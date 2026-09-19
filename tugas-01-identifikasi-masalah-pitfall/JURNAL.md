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
  
- Muhammad Naufal Sniper H mengomentari analisis Aziz Faadihillah: pembahasan Latency is Zero sudah sesuai karena skenario menyebutkan modul pesanan menunggu respons pembayaran tanpa batas waktu. Bagian trade-off diperjelas dengan menambahkan risiko retry yang dapat menambah beban server.

- Riandhika Bagus Rosdyantoro mengomentari analisis Muhammad Naufal Sniper H: pembahasan Single Point of Failure sudah sesuai dengan kondisi satu server yang menangani seluruh modul. Bagian solusi diperjelas agar tetap realistis dan sesuai dengan kebutuhan FoodGo.
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17 September 2026 | ChatGPT | Meminta bantuan mencari pitfall yang kemungkinan relevan dari skenario FoodGo. | AI menyarankan beberapa kandidat pitfall seperti Latency is zero, The Network is Reliable, dan Single Point of Failure. | Kelompok mencocokkan kandidat tersebut dengan kalimat spesifik pada skenario. Setelah diskusi, kelompok memilih tiga pitfall yang paling sesuai dan masing-masing anggota mengembangkan analisisnya sendiri. |
| 17 September 2026 | ChatGPT | Apa saja hal yang perlu diperhatikan saat membahas pitfall *The Network is Reliable* pada kasus FoodGo? | AI memberikan beberapa poin yang dapat dipertimbangkan, seperti kemungkinan gangguan jaringan, perlunya timeout dan retry, serta risiko retry yang berlebihan. | Poin tersebut digunakan sebagai bahan diskusi. Kami menentukan sendiri hubungan antara pitfall dengan skenario FoodGo, kemudian menyusun penjelasan, dampak, solusi, dan trade-off dengan bahasa sendiri. |
| 17 September 2026 | ChatGPT | Apa saja hal yang perlu diperhatikan saat membahas *Single Point of Failure* pada arsitektur FoodGo yang menggunakan satu server? | AI memberikan ide bahwa penggunaan satu server untuk beberapa modul dapat menjadi titik kegagalan dan menyarankan beberapa konsep yang dapat dipertimbangkan, seperti pemisahan service dan load balancing. | Ide tersebut digunakan sebagai bahan diskusi kelompok. Analisis akhir disesuaikan dengan skenario FoodGo dan dikembangkan sendiri, termasuk penjelasan dampak, solusi desain, dan trade-off. |
| 19 September 2026 | ChatGPT | Meminta bantuan mengidentifikasi pitfall yang sesuai dengan skenario FoodGo untuk bagian yang diambil yaitu Latency is zero. | AI menyarankan Latency is zero karena skenario menyebut modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu karena tidak ada timeout. | Kelompok mencocokkan saran tersebut dengan kalimat spesifik pada skenario, lalu membahas bareng penyebab, dampak ke FoodGo, solusi, dan trade-off berdasarkan hasil diskusi kelompok. |
