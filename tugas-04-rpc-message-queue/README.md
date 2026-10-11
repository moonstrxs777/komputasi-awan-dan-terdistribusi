# Tugas 4 (Pekan 4) — Komunikasi Antar Komponen

**Materi terkait:** Remote Procedure Call (RPC), Message-Oriented Middleware (MOM)/Message Queue.

## Studi Kasus

Modul **Pembayaran** dan modul **Pesanan** FoodGo harus berkomunikasi secara reliabel. Untuk beberapa operasi (mis. cek status saldo) respons dibutuhkan **seketika** (sinkron). Untuk operasi lain (mis. kirim notifikasi "pembayaran berhasil" ke modul kurir) sistem **tidak boleh menunggu** — modul pembayaran harus tetap responsif walau modul kurir sedang sibuk/down (asinkron).

## Pilihan Tugas

Kelompok **wajib memilih salah satu jalur** di bawah (boleh mengerjakan keduanya untuk nilai eksplorasi tambahan, tapi minimal satu harus selesai penuh dengan bukti jalan):

### Jalur A — RPC (Sinkron)

Skeleton di folder `rpc/` memakai `xmlrpc` — bagian dari Python standard library, **tidak perlu install apa pun**.

- `rpc/server.py`: mensimulasikan modul Pembayaran, expose fungsi `cek_saldo(user_id)` dan `proses_pembayaran(user_id, jumlah)` lewat RPC.
- `rpc/client.py`: mensimulasikan modul Pesanan yang memanggil fungsi RPC di atas dan menunggu hasilnya.

Jalankan (dua terminal terpisah, di laptop yang sama):
```bash
python3 rpc/server.py      # terminal 1
python3 rpc/client.py      # terminal 2
```

### Jalur B — Message Queue / MOM (Asinkron)

Skeleton di folder `mq/` memakai **RabbitMQ** yang dijalankan **lokal lewat Docker** (image resmi RabbitMQ, gratis, tidak perlu daftar akun apa pun) + library Python `pika`.

```bash
cd mq
docker compose up -d           # jalankan broker RabbitMQ lokal
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 consumer.py            # terminal 1: jalankan dulu consumer (modul kurir)
python3 publisher.py           # terminal 2: kirim event (modul pembayaran)
```

- `mq/publisher.py`: mensimulasikan modul Pembayaran yang mem-publish event `pembayaran_berhasil` tanpa menunggu balasan.
- `mq/consumer.py`: mensimulasikan modul Kurir/Notifikasi yang subscribe dan memproses event tersebut kapan pun siap.

Dashboard manajemen RabbitMQ (untuk lihat antrean secara visual) otomatis aktif di `http://localhost:15672` (login default `guest`/`guest`) — sertakan screenshot dashboard ini sebagai bukti tambahan.

## Tugas Kelompok

1. Lengkapi bagian `# TODO` di jalur yang dipilih.
2. Buktikan program benar-benar berjalan (screenshot 2 terminal berdampingan, atau video).
3. Untuk Jalur B, matikan dulu `consumer.py`, jalankan `publisher.py` beberapa kali, lalu nyalakan `consumer.py` — buktikan pesan **tetap diproses** (tidak hilang) karena antrean menyimpannya. Ini adalah inti pembelajaran *asynchronous decoupling*.
4. Tulis analisis: kenapa jalur ini (RPC atau MQ) cocok untuk skenario yang kalian pilih, dan apa yang terjadi jika dipakai untuk skenario yang salah (mis. RPC dipakai untuk notifikasi kurir → modul pembayaran ikut lambat kalau kurir down).

## Struktur Submission

```
tugas-04-rpc-message-queue/
├── README.md      # Analisis: kenapa sinkron/asinkron, hasil uji "pesan tidak hilang"
├── JURNAL.md
├── rpc/            # Jalur A (jika dikerjakan)
├── mq/             # Jalur B (jika dikerjakan)
└── bukti/
```
## Analisis

Pada studi kasus FoodGo, RPC cocok digunakan untuk komunikasi antara modul Pesanan dan Pembayaran, terutama untuk proses yang membutuhkan respons langsung, seperti cek saldo dan pembayaran. Dengan RPC, modul Pesanan bisa memanggil fungsi cek_saldo() atau proses_pembayaran() di modul Pembayaran, lalu menunggu hasilnya sebelum melanjutkan proses. Namun, karena kelompok kami memilih Jalur B, RPC tidak diuji secara langsung dan hanya dibahas sebagai pembanding.

Sementara itu, Message Queue lebih cocok digunakan untuk mengirim notifikasi pembayaran berhasil dari modul Pembayaran ke modul Kurir/Notifikasi. Dalam hal ini, modul Pembayaran tidak perlu menunggu respons dari modul Kurir karena pesan bisa diproses nanti saat consumer sudah aktif. RabbitMQ digunakan sebagai perantara untuk menyimpan pesan sementara. Dari hasil pengujian, saat consumer dimatikan, publisher yang dijalankan dua kali tetap berhasil mengirim enam pesan. Di RabbitMQ terlihat Ready = 6, Persistent = 6, dan Consumers = 0. Setelah consumer dinyalakan kembali, keenam pesan berhasil diproses hingga jumlah Ready menjadi 0. Dari percobaan ini, bisa dilihat bahwa modul Pembayaran tetap bisa berjalan meskipun modul Kurir sedang tidak tersedia.

Kalau pola komunikasi yang digunakan tidak sesuai dengan kebutuhan, sistem bisa menjadi kurang efisien, prosesnya lebih lambat, atau bahkan terganggu saat salah satu modul bermasalah. Misalnya, jika RPC digunakan untuk mengirim notifikasi pembayaran ke kurir, modul Pembayaran harus menunggu respons dari modul Kurir. Kalau modul Kurir sedang down atau lambat, proses pembayaran bisa ikut tertunda. Sebaliknya, jika Message Queue digunakan untuk pengecekan saldo yang membutuhkan hasil langsung, prosesnya menjadi kurang praktis karena modul Pesanan tidak bisa langsung mendapatkan hasil seperti saat menggunakan RPC.

Kesimpulan : Untuk FoodGo, cek saldo memakai RPC karena butuh jawaban seketika, sedangkan notifikasi pembayaran ke kurir memakai Message Queue agar Pembayaran tetap responsif dan tidak ada pesan yang hilang walau kurir sedang mati.

## Rubrik Penilaian (Tugas 4)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi berjalan (minimal 1 jalur) | 35% | RPC call sukses dapat balasan, ATAU pesan MQ sukses dikonsumsi |
| Bukti *asynchronous decoupling* (khusus Jalur B) / bukti sinkron blocking (Jalur A) | 25% | Skenario consumer mati lalu nyala lagi (B), atau bukti client menunggu response (A) |
| Analisis pemilihan pola komunikasi | 25% | Justifikasi tepat berdasarkan kebutuhan sinkron vs asinkron di skenario |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum RPC/message queue ke AI; **tidak boleh** meminta AI menuliskan isi `# TODO` di `rpc/server.py`, `rpc/client.py`, `mq/publisher.py`, atau `mq/consumer.py`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `JURNAL.md` wajib menjelaskan apa yang terjadi pada request RPC jika server mati di tengah proses (Jalur A), atau ke mana pesan "hilang sementara" tersimpan saat consumer mati (Jalur B) — jawaban generik/hafalan istilah tanpa mengaitkan ke hasil percobaan sendiri akan dinilai rendah.
