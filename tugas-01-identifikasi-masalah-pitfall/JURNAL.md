# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [17 SEPTEMBER 2026]
- Peserta: Aziz Faadhilah , Riandhika Bagus , Muhammad Naufal Sniper H
- Poin diskusi: - Kami membahas penyebab FoodGo bermasalah saat trafik naik. Dari skenario, kami menemukan dua hal yang paling jelas, yaitu semua modul berjalan dalam satu server dan adanya asumsi bahwa jaringan selalu reliable.
                - Untuk bagian single point of failure, kami sepakat bahwa satu server yang menangani pesanan, pembayaran, dan notifikasi kurir membuat beberapa fungsi ikut terdampak ketika server tersebut crash.
                - Pada bagian the network is reliable, kami membahas bahwa request antar-service bisa mengalami gangguan atau terlambat. Karena tidak ada retry dan timeout, request yang menunggu dapat membuat resource semakin terbebani.
                - Untuk solusi, kami sepakat bahwa FoodGo bisa memisahkan service secara bertahap dan menambahkan timeout serta retry yang dibatasi. Kami juga mencatat bahwa solusi tersebut membuat sistem lebih kompleks untuk dikelola.
- Perbedaan pendapat (jika ada): ...

## [Tanggal diskusi 2]
- ...

## Review Silang
- [Nama] mengomentari analisis [Nama lain]: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
