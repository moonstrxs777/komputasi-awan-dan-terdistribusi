
"""
Tugas 7 (opsional) - Simulasi Replikasi Dua Server (Jakarta & Bandung)

Mensimulasikan delay replikasi dan masalah inconsistent read,
lalu memperbaikinya dengan mekanisme Read-Your-Writes sederhana.
"""

import time
import threading

REPLICATION_DELAY = 2.0  # detik, simulasi lambatnya sinkronisasi antar server


class Replica:
    def __init__(self, name: str):
        self.name = name
        self.saldo: dict[str, float] = {}
        self.last_write_version: dict[str, int] = {}

    def write(self, user_id: str, saldo_baru: float, version: int):
        # Menyimpan saldo terbaru dan nomor versi ke replika
        self.saldo[user_id] = saldo_baru
        self.last_write_version[user_id] = version

        print(
            f"[{self.name}] WRITE saldo {user_id} = "
            f"{saldo_baru} (versi {version})"
        )

    def read(self, user_id: str) -> float:
        # Membaca saldo pelanggan dari replika
        return self.saldo.get(user_id, 0.0)


class ReplicationSystem:
    def __init__(self):
        # Membuat dua replika server, yaitu Jakarta dan Bandung
        self.jakarta = Replica("Jakarta")
        self.bandung = Replica("Bandung")
        self.version_counter = 0

    def top_up(self, user_id: str, jumlah: float):
        """Top-up selalu ditulis dulu ke server Jakarta (mis. server terdekat pelanggan)."""

        # Setiap perubahan saldo memiliki nomor versi baru
        self.version_counter += 1
        version = self.version_counter

        # Menghitung saldo baru berdasarkan saldo sebelumnya
        saldo_baru = self.jakarta.read(user_id) + jumlah

        # Menyimpan perubahan saldo pada server Jakarta
        self.jakarta.write(user_id, saldo_baru, version)

        # TODO 1: replikasi ke Bandung TERTUNDA (simulasikan dengan
        # threading.Timer(REPLICATION_DELAY, ...) yang memanggil
        # self.bandung.write(user_id, saldo_baru, version) setelah delay.

        # Menjalankan proses replikasi secara terpisah dengan delay 2 detik
        threading.Timer(
            REPLICATION_DELAY,
            self.bandung.write,
            args=(user_id, saldo_baru, version)
        ).start()

        print(
            f"[TODO] Replikasi ke Bandung akan tertunda "
            f"{REPLICATION_DELAY} detik"
        )

        return version

    def baca_saldo_naif(self, user_id: str, server: str) -> float:
        """Baca saldo TANPA mekanisme Read-Your-Writes - bisa saja stale."""

        # Memilih server berdasarkan lokasi yang diminta
        replica = self.jakarta if server == "Jakarta" else self.bandung

        # Langsung membaca saldo tanpa memeriksa nomor versi
        return replica.read(user_id)

    def baca_saldo_read_your_writes(
        self, user_id: str, server: str, versi_minimal: int
    ) -> float:
        """Implementasikan Read-Your-Writes -
        jika replika yang dituju versi datanya < versi_minimal (client pernah
        melihat versi lebih baru sebelumnya), tunggu/redirect ke replika yang
        sudah punya versi tersebut (di sini cukup simulasikan dengan polling
        sampai versi replika >= versi_minimal, atau redirect ke Jakarta)."""

        # Memilih replika yang akan digunakan untuk membaca saldo
        replica = self.jakarta if server == "Jakarta" else self.bandung

        # TODO 2: memeriksa apakah versi replika sudah sesuai
        versi_lokal = replica.last_write_version.get(user_id, 0)

        # Jika versi lokal masih tertinggal, pelanggan harus menunggu
        # sampai proses replikasi selesai dan versi yang dibutuhkan tersedia
        while versi_lokal < versi_minimal:

            print(
                f"{server} versi {versi_lokal} < "
                f"{versi_minimal} menunggu replikasi"
            )

            # Memberikan jeda sebelum melakukan pemeriksaan ulang
            time.sleep(0.1)

            # Memeriksa kembali versi terbaru pada replika
            versi_lokal = replica.last_write_version.get(user_id, 0)

        # Setelah versi sesuai, saldo terbaru dapat dibaca
        print(f"[{server}] Data sudah tersinkronisasi.")

        return replica.read(user_id)


def main():
    system = ReplicationSystem()
    user_id = "user1"

    print("=== SIMULASI REPLIKASI FOODGO ===")

    print("\n--- Skenario 1: Tanpa Read-Your-Writes ---")

    # Pelanggan melakukan top-up Rp50.000 melalui Jakarta
    system.top_up(user_id, 50000)

    # Pelanggan langsung membaca saldo sebelum replikasi selesai
    time.sleep(0.5)

    saldo_naif = system.baca_saldo_naif(user_id, "Bandung")

    print("Saldo yang terbaca di Bandung:", saldo_naif)
    print("-> Terjadi inconsistent read karena saldo belum tersinkronisasi.")

    # Menunggu agar replikasi pertama selesai sebelum skenario berikutnya
    time.sleep(REPLICATION_DELAY + 0.5)

    print("\n--- Skenario 2: Dengan Read-Your-Writes ---")

    # Pelanggan melakukan top-up tambahan Rp20.000 melalui Jakarta
    versi_terakhir = system.top_up(user_id, 20000)

    # TODO 3: memanggil Read-Your-Writes dan menunjukkan hasilnya
    # walau dipanggil segera setelah top_up (< REPLICATION_DELAY detik).

    # Membaca saldo melalui Bandung dengan versi minimal yang dibutuhkan
    saldo = system.baca_saldo_read_your_writes(
        user_id,
        "Bandung",
        versi_terakhir
    )

    print("Saldo yang terbaca di Bandung:", saldo)
    print("-> Saldo berhasil dibaca setelah versi terbaru diterima.")

    # Menunggu agar proses replikasi terakhir selesai sebelum program berakhir
    time.sleep(REPLICATION_DELAY + 0.5)

    print("\n=== SIMULASI SELESAI ===")


if __name__ == "__main__":
    main()
