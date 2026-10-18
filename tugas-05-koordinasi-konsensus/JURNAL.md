# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: Pesan **OK** datang lewat koneksi terpisah, sehingga kami memakai **threading.Event** untuk menunggunya, dan **start_election()** dijalankan di thread terpisah supaya handler pesan tidak terblokir selama **ELECTION_TIMEOUT**. Node 4 menerima **ELECTION** dari beberapa node sekaligus sehingga election bisa berjalan ganda, dan kami mengatasinya dengan flag **electing**. Saat pengujian start bertahap, pengumuman **COORDINATOR** dari node ber-ID lebih kecil sempat membuat node 5 salah mencatat leader, sehingga kami menambahkan aturan untuk mengabaikan **COORDINATOR** dari node ber-ID lebih kecil dan memulai election. Selain itu, di Windows perintah **python3** tidak dikenali sehingga kami memakai **python**.

## Skenario 1: Start normal
- Leader yang terpilih: Node 5 (ID tertinggi).
- Log/observasi: Node 1-4 mengirim **ELECTION** ke node ber-ID lebih tinggi dan menerima **OK**, sehingga berhenti mencalonkan diri. Node 5 tidak menerima **OK**, menyatakan diri leader, lalu broadcast **COORDINATOR**, dan node 1-4 mencatat **Leader sekarang adalah node 5**. Karena node dinyalakan bergantian, node 4 sempat menjadi leader sementara sebelum node 5 aktif, lalu digantikan oleh node 5. Bukti: **bukti/skenario1_start_normal.png.**

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: Node 4 (ID tertinggi yang masih hidup setelah node 5 dihentikan dengan Ctrl+C). Bukti: **bukti/skenario2_leader_mati.png.**
- Berapa lama waktu sampai leader baru terdeteksi: Sekitar 3-5 detik, yaitu paling lama 3 detik menunggu pengecekan ping berkala (**monitor_leader**) ditambah 2 detik **ELECTION_TIMEOUT** menunggu **OK**. Angka ini perkiraan dari konfigurasi program karena log kami tidak memuat timestamp, dan pada pengujian leader baru terlihat dalam beberapa detik tanpa campur tangan manual.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
