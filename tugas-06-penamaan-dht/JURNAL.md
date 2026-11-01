# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui: _(isi sesuai pengalaman kelompok)_. Contoh jebakan umum: `min(candidates)` error/mengembalikan `None` saat tidak ada node dengan id ≥ key (lupa wrap-around), misalnya untuk `kurir-006` (hash 217 > semua id node).
- Cara memperbaikinya: jika daftar kandidat kosong, kembalikan `min(self.nodes)` (node dengan id terkecil), karena ring melingkar.

## Skenario join/leave
- Pemilihan skenario: nama node awal `node-medan-1` (id=123) ternyata tidak memindahkan key apa pun, dan `node-jakarta-1` (id=177) yang keluar tidak memegang data, sehingga perpindahan tidak terlihat. Diganti `node-makassar-1` (id=63) untuk join dan `node-surabaya-1` (id=136) untuk leave.
- Hasil sebelum & sesudah node baru bergabung: sebelum, `kurir-001` (h=50) dipegang node 102. Sesudah `node-makassar-1` (id=63) join, `kurir-001` pindah ke node 63; lookup tetap `192.168.1.10`.
- Hasil sebelum & sesudah node keluar: sebelum, `kurir-003` (h=132) dipegang node 136. Sesudah node 136 keluar, `kurir-003` pindah ke successor baru (node 177); lookup tetap `192.168.1.12`.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
