# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [17 SEPTEMBER 2026]
- Peserta: Aziz Faadhilah , Riandhika Bagus , Muhammad Naufal Sniper H
- Poin diskusi:
    -  Kami membahas penyebab FoodGo bermasalah saat trafik naik. Dari skenario, kami menemukan dua hal yang paling jelas, yaitu semua modul berjalan dalam satu server dan adanya asumsi bahwa jaringan selalu reliable.
    -  Untuk bagian single point of failure, kami sepakat bahwa satu server yang menangani pesanan, pembayaran, dan notifikasi kurir membuat beberapa fungsi ikut terdampak ketika server tersebut crash.
    -  Pada bagian the network is reliable, kami membahas bahwa request antar-service bisa mengalami gangguan atau terlambat. Karena tidak ada retry dan timeout, request yang menunggu dapat membuat resource semakin terbebani.
    -  Untuk solusi, kami sepakat bahwa FoodGo bisa memisahkan service secara bertahap dan menambahkan timeout serta retry yang dibatasi. Kami juga mencatat bahwa solusi tersebut membuat sistem lebih kompleks untuk dikelola.
- Perbedaan pendapat (jika ada): ...

## [19 SEPTEMBER 2026]
- Peserta: Aziz Faadhilah, Riandhika Bagus, Muhammad Naufal Sniper H
- Poin diskusi:
  - Kami melakukan pengecekan ulang terhadap hasil pengerjaan yang sudah dibuat sebelumnya untuk melihat bagian yang masih kurang atau kurang tepat.
  - Dari hasil pengecekan, beberapa bagian diperbaiki dan dilengkapi agar pembahasannya lebih sesuai dengan skenario FoodGo.
  - Untuk setiap pitfall, dibahas kembali hubungan antara masalah yang terjadi, dampaknya terhadap sistem, serta solusi yang dapat diterapkan.
  - Bagian kesimpulan kelompok kemudian disusun berdasarkan hasil analisis dan pembahasan yang telah disepakati.
  - Terakhir, JURNAL.md dilengkapi dan dirapikan agar proses diskusi dan pengerjaan kelompok terdokumentasi dengan baik.
- Perbedaan pendapat (jika ada): 

## Review Silang
- Aziz Faadihillah mengomentari analisis Riandhika Bagus Rosdyantoro: pembahasan tentang The Network is Reliable sudah sesuai dengan skenario. Bagian dampak diperjelas agar hubungan antara gangguan jaringan, request yang menumpuk, dan beban server lebih terlihat.

- Riandhika Bagus Rosdyantoro mengomentari analisis Muhammad Naufal Sniper H: pembahasan Single Point of Failure sudah sesuai dengan kondisi satu server yang menangani seluruh modul. Bagian solusi diperjelas agar tetap realistis dan sesuai dengan kebutuhan FoodGo.

- Muhammad Naufal Sniper H mengomentari analisis Aziz Faadihillah: pembahasan Latency is Zero sudah sesuai karena skenario menyebutkan modul pesanan menunggu respons pembayaran tanpa batas waktu. Bagian trade-off diperjelas dengan menambahkan risiko retry yang dapat menambah beban server.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
