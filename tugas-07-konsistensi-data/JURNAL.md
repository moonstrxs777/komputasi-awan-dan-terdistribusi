# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi

- **Argumen yang dipertimbangkan:** Kelompok membahas perbedaan Sequential Consistency dan Eventual Consistency pada sistem terdistribusi. Pada kasus FoodGo, keterlambatan replikasi menyebabkan server Jakarta dan Bandung memiliki informasi saldo yang berbeda. Hal ini dapat menyebabkan transaksi pelanggan ditolak meskipun saldo sebenarnya mencukupi. Kelompok juga mempertimbangkan bahwa data keuangan lebih sensitif terhadap keterlambatan pembaruan dibandingkan data seperti jumlah like di media sosial.

- **Kesimpulan akhir & alasan:** Kelompok menyimpulkan bahwa Eventual Consistency saja tidak cukup untuk menangani permasalahan saldo FoodGo. Penerapan Sequential Consistency secara menyeluruh juga belum tentu diperlukan karena dapat menambah waktu komunikasi antarserver. Oleh karena itu, kelompok memilih pendekatan Client-Centric Consistency berupa Read-Your-Writes agar pelanggan tetap dapat melihat saldo terbaru setelah melakukan top-up meskipun berpindah server.

## Simulasi (jika dikerjakan)

- **Hasil skenario naif vs Read-Your-Writes:**

  Pada skenario naif, pelanggan melakukan top-up sebesar Rp50.000 melalui server Jakarta. Namun, karena terdapat delay replikasi selama 2 detik, server Bandung masih membaca saldo Rp0 ketika pelanggan langsung melakukan pembacaan. Kondisi ini menunjukkan terjadinya *inconsistent read*.

  Pada skenario Read-Your-Writes, pelanggan melakukan top-up tambahan sebesar Rp20.000 sehingga saldo menjadi Rp70.000. Sistem menggunakan nomor versi untuk memeriksa apakah data pada server Bandung sudah diperbarui. Jika versi Bandung masih tertinggal, sistem akan menunggu proses replikasi sampai versi yang dibutuhkan tersedia. Setelah replikasi selesai, saldo yang terbaca di Bandung menjadi Rp70.000 dengan versi terbaru.

  Dari hasil simulasi, mekanisme Read-Your-Writes dapat membantu mengatasi masalah pembacaan saldo lama akibat keterlambatan replikasi.

## Log Penggunaan AI (Level 2)

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 15 November 2026 | ChatGPT | Menjelaskan perbedaan Sequential Consistency dan Eventual Consistency pada kasus saldo e-wallet FoodGo. | Memahami bahwa data saldo lebih sensitif terhadap keterlambatan replikasi karena berkaitan dengan transaksi keuangan. | Kelompok membahas kembali dampaknya dan menentukan pendekatan konsistensi yang sesuai dengan kasus FoodGo. |
| 15 November 2026 | ChatGPT | Membahas penerapan Read-Your-Writes menggunakan nomor versi pada dua server. | Mendapatkan gambaran penggunaan version untuk memastikan pelanggan membaca perubahan saldo terbarunya sendiri. | Kelompok mempelajari alur penggunaan nomor versi dan menyesuaikannya dengan studi kasus FoodGo. |
| 15 November 2026 | ChatGPT | Meminta bantuan memahami dan melengkapi simulasi replikasi pada file `replica_simulation.py`. | Mendapatkan referensi penggunaan `threading.Timer`, delay replikasi, dan polling versi untuk simulasi Read-Your-Writes. | Kelompok meninjau kode, memahami fungsi setiap bagian, dan menjalankan simulasi untuk memeriksa hasil pembacaan saldo sebelum dan sesudah replikasi. |
| 15 November 2026 | ChatGPT | Meminta bantuan menyusun penjelasan hasil simulasi dan format dokumentasi tugas. | Mendapatkan gambaran cara menjelaskan kondisi inconsistent read dan perbaikan menggunakan Read-Your-Writes. | Penjelasan disesuaikan dengan hasil simulasi dan kebutuhan dokumentasi README.md serta JURNAL.md. |

