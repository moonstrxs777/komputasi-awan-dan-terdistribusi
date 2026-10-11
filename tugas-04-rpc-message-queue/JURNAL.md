# Jurnal Proses — Tugas 4

## Jalur yang dipilih
  Jalur B (Message Queue / RabbitMQ).
  
  Alasan: skenario notifikasi "pembayaran berhasil" ke modul kurir tidak butuh
  balasan seketika, jadi lebih cocok asinkron. Modul pembayaran tidak boleh ikut
  lambat kalau kurir sedang sibuk atau down.
  
## Kendala teknis
1. *Docker belum jalan.* docker compose up -d gagal dengan pesan
   "failed to connect to the docker API". Solusi: buka Docker Desktop dan tunggu
   status Engine running, lalu jalankan ulang.
2. *ModuleNotFoundError: No module named 'pika'.* Terjadi karena program
   dijalankan dengan tombol Run VS Code / terminal tanpa venv aktif, sehingga
   memakai Python global. Solusi: aktifkan venv\Scripts\activate lalu jalankan
   lewat terminal.
3. *Output masih [TODO] Event belum benar-benar terkirim.* publisher.py
   belum diganti ke versi yang sudah diisi. Solusi: lengkapi TODO 1-4 dan ganti
   log menjadi Event terkirim.
4. *Folder proyek belum repo Git* (berasal dari unduhan ZIP). Solusi: dibuat/
   dihubungkan ke repo Git sebelum commit.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
