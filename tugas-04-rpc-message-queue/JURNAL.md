# Jurnal Proses — Tugas 4

## Jalur yang dipilih
Jalur B (Message Queue / RabbitMQ).

Alasan: notifikasi pembayaran berhasil ke modul kurir tidak memerlukan balasan secara langsung, sehingga lebih sesuai menggunakan komunikasi asinkron. Dengan cara ini, proses pembayaran tetap dapat berjalan tanpa harus menunggu modul kurir selesai memproses pesan, termasuk ketika modul kurir sedang sibuk atau tidak aktif.
  
## Kendala teknis
1. **Docker tidak dapat dijalankan.** Saat menjalankan docker compose up -d, muncul pesan error failed to connect to the docker API. Solusi: membuka Docker Desktop, menunggu hingga Docker Engine berjalan, kemudian menjalankan kembali perintah tersebut.
2. **ModuleNotFoundError:** No module named 'pika'. Error terjadi karena program dijalankan menggunakan Python global ketika virtual environment belum aktif. Solusi: mengaktifkan virtual environment melalui perintah venv\Scripts\activate, kemudian menjalankan program melalui terminal.
3. **Output masih menunjukkan [TODO].** Pada pengujian awal, publisher belum menjalankan proses pengiriman pesan karena bagian kode yang diperlukan belum dilengkapi. Solusi: menyelesaikan bagian TODO sesuai instruksi tugas, kemudian menjalankan kembali publisher untuk memastikan event berhasil dikirim.
4. **Folder proyek belum terhubung ke repository Git.** Proyek awalnya berasal dari unduhan ZIP sehingga belum terhubung ke repository. Solusi: membuat atau menghubungkan repository Git sebelum melakukan commit dan push perubahan.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: Menghentikan consumer → menjalankan publisher sebanyak dua kali → memeriksa dashboard RabbitMQ → menjalankan kembali consumer.

- Hasil yang diamati:

   - Publisher berhasil mengirimkan total 6 event meskipun consumer sedang tidak aktif.

   - Dashboard menunjukkan Ready = 6, Persistent = 6, dan Consumers = 0. Queue telah dikonfigurasi dengan durable: true.

   - Setelah consumer dijalankan kembali, keenam pesan berhasil diproses. Dashboard menunjukkan Ready = 0 dan Consumers = 1.

- Kesimpulan: Pesan tetap tersimpan di antrean RabbitMQ ketika consumer tidak aktif dan dapat diproses setelah consumer dijalankan kembali. Mekanisme basic_ack digunakan untuk memberi tahu RabbitMQ bahwa pesan telah selesai diproses sehingga dapat dihapus dari antrean.

- Bukti: Disimpan dalam folder bukti/ dengan nama berkas 00 sampai 05.
  
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10–11 Okt 2026 | Claude | Bertanya tentang cara kerja RPC dan Message Queue serta perbedaan keduanya. | Mendapat penjelasan mengenai komunikasi langsung pada RPC dan pengiriman pesan melalui queue pada Message Queue. | Penjelasan dipelajari kembali, lalu dibandingkan dengan hasil percobaan yang dilakukan saat mengerjakan tugas. |
| 10–11 Okt 2026 | Claude | Meminta arahan untuk mengatasi kendala saat menjalankan Docker, mengatur virtual environment, memasang pika, dan menggunakan Git. | Mendapat beberapa langkah untuk memeriksa penyebab error dan memperbaiki konfigurasi. | Langkah-langkah dicoba sendiri di laptop. Kendala yang muncul dan hasil setelah diperbaiki dicatat dalam jurnal. |
| 10–11 Okt 2026 | Claude | Bertanya tentang hal-hal yang perlu dibahas saat membandingkan RPC dan Message Queue dalam README. | Mendapat ide untuk membahas perbedaan alur komunikasi, respons, dan penanganan pesan ketika terjadi gangguan. | Pembahasan disusun berdasarkan pemahaman sendiri dan disesuaikan dengan hasil pengujian yang benar-benar dilakukan. |
