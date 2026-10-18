"""
Tugas 5 - Simulasi Node untuk Bully Algorithm

Infrastruktur jaringan (socket server/client) sudah disediakan.
Logika Bully Algorithm (bagian # TODO) harus kalian lengkapi sendiri.

Contoh menjalankan (5 terminal terpisah):
    python3 node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
    python3 node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
    ... dst untuk id 3, 4, 5
"""

import argparse
import socket
import threading
import time

ELECTION_TIMEOUT = 2.0  # detik menunggu balasan OK sebelum menyatakan diri leader


class Node:
    def __init__(self, node_id: int, port: int, peers: dict):
        self.node_id = node_id
        self.port = port
        # peers: dict {peer_id: peer_port} untuk semua node LAIN
        self.peers = peers
        self.leader_id = None
        self.lock = threading.Lock()
        # --- state tambahan untuk Bully Algorithm ---
        self.ok_event = threading.Event()           # diset saat menerima "OK"
        self.coordinator_event = threading.Event()  # diset saat menerima "COORDINATOR"
        self.electing = False                       # True selama election milik node ini berjalan

    def log(self, text: str):
        print(f"[Node {self.node_id}] {text}", flush=True)

    # ---------- Infrastruktur jaringan (SUDAH LENGKAP, jangan diubah) ----------

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", self.port))
        server.listen()
        print(f"[Node {self.node_id}] Listening di port {self.port}")
        while True:
            conn, _ = server.accept()
            threading.Thread(target=self.handle_connection, args=(conn,), daemon=True).start()

    def handle_connection(self, conn: socket.socket):
        with conn:
            data = conn.recv(1024).decode()
            if not data:
                return
            sender_id, msg_type = data.split(":")
            self.on_message(int(sender_id), msg_type)

    def send_message(self, target_port: int, msg_type: str) -> bool:
        """Kirim pesan ke node lain. Return False jika node target tidak merespons (dianggap mati)."""
        try:
            with socket.create_connection(("localhost", target_port), timeout=1.0) as s:
                s.sendall(f"{self.node_id}:{msg_type}".encode())
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    # ---------- Logika Bully Algorithm (LENGKAPI BAGIAN INI) ----------

    def on_message(self, sender_id: int, msg_type: str):
        """Dipanggil setiap kali node ini menerima pesan dari node lain."""
        if msg_type == "PING":
            return  # hanya untuk cek hidup/mati, tidak perlu dilog

        self.log(f"Menerima pesan '{msg_type}' dari node {sender_id}")

        if msg_type == "ELECTION":
            if self.node_id > sender_id:
                # Kita lebih besar -> "membully" pengirim: balas OK, lalu ikut election.
                self.send_message(self.peers[sender_id], "OK")
                # Jalankan di thread terpisah supaya handler tidak terblokir
                # selama ELECTION_TIMEOUT.
                threading.Thread(target=self.start_election, daemon=True).start()
        elif msg_type == "OK":
            # Ada node lebih tinggi yang hidup -> jangan jadi leader.
            self.ok_event.set()
        elif msg_type == "COORDINATOR":
            if sender_id < self.node_id:
                # Pengumuman dari node ber-id lebih kecil tidak boleh diterima:
                # kita lebih tinggi, jadi kita ambil alih lewat election.
                self.log(f"Mengabaikan COORDINATOR dari node {sender_id} (id lebih kecil), mulai election")
                threading.Thread(target=self.start_election, daemon=True).start()
                return
            with self.lock:
                self.leader_id = sender_id
            self.coordinator_event.set()
            self.log(f"Leader sekarang adalah node {sender_id}")

    def start_election(self):
        """Dipanggil saat node ini mendeteksi leader tidak ada / tidak merespons."""
        # Cegah dua election berjalan bersamaan di node yang sama.
        with self.lock:
            if self.electing:
                return
            self.electing = True

        try:
            while True:
                higher_peers = {pid: p for pid, p in self.peers.items() if pid > self.node_id}
                self.ok_event.clear()
                self.coordinator_event.clear()
                self.log(f"Memulai ELECTION ke peer lebih tinggi: {sorted(higher_peers)}")

                for pid, port in higher_peers.items():
                    if not self.send_message(port, "ELECTION"):
                        self.log(f"Node {pid} tidak merespons (dianggap mati)")

                # Tunggu balasan OK dari node yang lebih tinggi.
                if not self.ok_event.wait(timeout=ELECTION_TIMEOUT):
                    # Tidak ada yang lebih tinggi yang hidup -> kita leader.
                    self.declare_leader()
                    return

                # Ada node lebih tinggi yang hidup: berhenti mencalonkan diri,
                # tunggu pesan COORDINATOR darinya.
                self.log("Menerima OK, berhenti mencalonkan diri. Menunggu COORDINATOR...")
                if self.coordinator_event.wait(timeout=ELECTION_TIMEOUT * 3):
                    return
                # COORDINATOR tidak kunjung datang (node tinggi mati di tengah jalan)
                # -> ulangi election.
                self.log("COORDINATOR tidak datang, mengulang election")
        finally:
            with self.lock:
                self.electing = False

    def declare_leader(self):
        """Node ini menyatakan dirinya leader dan memberi tahu semua node lain."""
        with self.lock:
            self.leader_id = self.node_id
        self.log("*** Tidak ada OK. Saya menjadi LEADER, broadcast COORDINATOR ***")
        for pid, port in self.peers.items():
            if not self.send_message(port, "COORDINATOR"):
                self.log(f"Node {pid} mati/belum aktif, COORDINATOR tidak terkirim")

    def monitor_leader(self):
        """Loop periodik: cek apakah leader masih hidup, trigger election jika mati."""
        while True:
            time.sleep(3)
            with self.lock:
                leader = self.leader_id
                electing = self.electing
            if electing:
                continue  # sedang election, biarkan selesai dulu

            if leader is None:
                # Belum tahu siapa leader -> mulai election.
                threading.Thread(target=self.start_election, daemon=True).start()
            elif leader != self.node_id:
                if not self.send_message(self.peers[leader], "PING"):
                    self.log(f"Leader (node {leader}) tidak merespons! Memicu election baru")
                    with self.lock:
                        self.leader_id = None
                    threading.Thread(target=self.start_election, daemon=True).start()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--peers", type=str, required=True,
                         help="daftar port peer dipisah koma, mis. 5002,5003,5004,5005")
    args = parser.parse_args()

    # Asumsi konvensi port: id N selalu di port 5000+N (lihat contoh perintah di README).
    peer_ports = [int(p) for p in args.peers.split(",")]
    peers = {port - 5000: port for port in peer_ports}

    node = Node(args.id, args.port, peers)

    threading.Thread(target=node.start_server, daemon=True).start()
    threading.Thread(target=node.monitor_leader, daemon=True).start()

    time.sleep(1)  # beri waktu semua node lain start dulu sebelum election awal
    node.start_election()

    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()
