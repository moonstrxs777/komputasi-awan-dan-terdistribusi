"""
Tugas 6 - Simulasi Chord DHT (single-process, tanpa jaringan sungguhan)

Fungsi hashing & struktur data ring sudah disediakan.
Lengkapi TODO untuk lookup(), join(), dan leave().
"""

import hashlib

M_BITS = 8               # ruang identifier 0..255 (disederhanakan dari Chord asli yang pakai 160-bit)
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Hash string (ID node atau ID kurir) ke ruang identifier 0..RING_SIZE-1."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        # node_id (hasil hash) -> alamat IP node tersebut
        self.nodes: dict[int, str] = {}
        # key kurir (hasil hash) -> IP kurir yang disimpan node yang bertanggung jawab
        self.data: dict[int, tuple[str, str]] = {}  # hash -> (kurir_id, ip_kurir)
        # key kurir (hash) -> node_id yang SAAT INI memegang data tsb.
        # Dipakai untuk melacak perpindahan tanggung jawab saat join/leave.
        self.owner: dict[int, int] = {}

    def join(self, node_name: str, node_ip: str):
        """Tambahkan node baru ke ring. Pindahkan data yang seharusnya
        menjadi tanggung jawab node baru ini dari successor lamanya."""
        node_id = hash_id(node_name)

        if node_id in self.nodes:
            raise ValueError(f"Tabrakan hash: id={node_id} sudah dipakai node {self.nodes[node_id]}")

        # TODO 2: successor LAMA dicari sebelum node baru dimasukkan ke self.nodes
        old_succ = self.find_successor(node_id) if self.nodes else None

        # TODO 1: daftarkan node baru
        self.nodes[node_id] = node_ip
        print(f"[JOIN] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")

        # TODO 3: key yang dipegang successor lama tetapi sekarang successor-nya
        # adalah node baru -> tanggung jawab berpindah ke node baru.
        if old_succ is None:
            return
        for key_hash in sorted(self.data):
            if self.owner.get(key_hash) == old_succ and self.find_successor(key_hash) == node_id:
                kurir_id, _ = self.data[key_hash]
                self.owner[key_hash] = node_id
                print(f"       -> key '{kurir_id}' (hash={key_hash}) pindah: "
                      f"node id={old_succ} ({self.nodes[old_succ]}) => node id={node_id} ({node_ip})")

    def leave(self, node_name: str):
        """Keluarkan sebuah node dari ring. Data yang dipegangnya harus
        berpindah ke successor-nya."""
        node_id = hash_id(node_name)

        if node_id not in self.nodes:
            print(f"[LEAVE] Node '{node_name}' tidak ada di ring")
            return

        # TODO 4: hapus node dari ring
        leaving_ip = self.nodes.pop(node_id)
        print(f"[LEAVE] Node '{node_name}' (id={node_id}, {leaving_ip}) keluar dari ring")

        # TODO 5: successor BARU untuk tiap key yang dipegang node ini
        for key_hash in sorted(self.data):
            if self.owner.get(key_hash) != node_id:
                continue
            kurir_id, _ = self.data[key_hash]
            if not self.nodes:
                del self.owner[key_hash]
                print(f"       -> key '{kurir_id}' hilang (ring kosong)")
                continue
            new_owner = self.find_successor(key_hash)
            self.owner[key_hash] = new_owner
            print(f"       -> key '{kurir_id}' (hash={key_hash}) pindah: "
                  f"node id={node_id} ({leaving_ip}) => node id={new_owner} ({self.nodes[new_owner]})")

    def find_successor(self, key_hash: int) -> int:
        """Cari node_id dengan nilai hash TERKECIL yang >= key_hash
        (successor menurut aturan Chord). Jika tidak ada, wrap-around
        ke node dengan hash terkecil di ring (karena ring melingkar)."""
        if not self.nodes:
            raise RuntimeError("Ring kosong, tidak ada node")
        # TODO 6: kandidat = node dengan id >= key_hash; ambil yang terkecil.
        candidates = [nid for nid in self.nodes if nid >= key_hash]
        if candidates:
            return min(candidates)
        # Wrap-around: key lebih besar dari semua node -> node dengan id terkecil.
        return min(self.nodes)

    def register_kurir(self, kurir_id: str, ip_kurir: str):
        """Simpan mapping ID Kurir -> IP di node yang bertanggung jawab."""
        key_hash = hash_id(kurir_id)
        # TODO 7: tentukan node penanggung jawab lalu simpan datanya
        node_id = self.find_successor(key_hash)
        self.data[key_hash] = (kurir_id, ip_kurir)
        self.owner[key_hash] = node_id
        print(f"[REGISTER] '{kurir_id}' (hash={key_hash}) -> {ip_kurir}, "
              f"disimpan di node id={node_id} ({self.nodes[node_id]})")

    def lookup(self, kurir_id: str) -> str | None:
        """Cari alamat IP terkini untuk sebuah ID Kurir."""
        key_hash = hash_id(kurir_id)
        # TODO 8: temukan node penanggung jawab, lalu ambil ip dari data-nya
        node_id = self.find_successor(key_hash)
        if self.owner.get(key_hash) != node_id or key_hash not in self.data:
            return None
        return self.data[key_hash][1]

    def show_ring(self):
        """Cetak isi ring berurutan beserta key yang dipegang tiap node."""
        print("  Ring (urut id):")
        for nid in sorted(self.nodes):
            keys = [f"{self.data[k][0]}(h={k})" for k in sorted(self.data) if self.owner.get(k) == nid]
            print(f"    id={nid:3d}  {self.nodes[nid]:<9} memegang: {', '.join(keys) or '-'}")


LEAVING = "node-surabaya-1"


def main():
    ring = ChordRing()

    # Skenario awal: 4 node bergabung
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")

    # Daftarkan beberapa kurir
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")
    # hash 217 > semua id node -> menguji wrap-around ke node dengan id terkecil
    ring.register_kurir("kurir-006", "192.168.1.15")

    print("\n--- Kondisi ring awal ---")
    ring.show_ring()

    print("\n--- Lookup sebelum perubahan topologi ---")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))

    print("\n--- Node baru bergabung ---")
    ring.join("node-makassar-1", "10.0.0.5")
    ring.show_ring()
    for k in ("kurir-001", "kurir-002", "kurir-003", "kurir-006"):
        print(k, "->", ring.lookup(k))

    print("\n--- Sebuah node keluar ---")
    ring.leave(LEAVING)
    ring.show_ring()
    for k in ("kurir-001", "kurir-002", "kurir-003", "kurir-006"):
        print(k, "->", ring.lookup(k))


if __name__ == "__main__":
    main()
