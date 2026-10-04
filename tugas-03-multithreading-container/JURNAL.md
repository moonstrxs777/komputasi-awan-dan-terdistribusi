# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
Pada percobaan pertama, program dijalankan tanpa menggunakan `Lock` pada
variabel `processed_count`. Program menggunakan 100 pesanan dan 10 thread
pekerja.

Program dijalankan sebanyak 5 kali untuk melihat apakah terjadi perbedaan
hasil akibat akses bersamaan terhadap `processed_count`.

| Percobaan | Hasil `processed_count` | Seharusnya |
|---|---:|---:|
| 1 | 10 | 100 |
| 2 | 10 | 100 |
| 3 | 10 | 100 |
| 4 | 10 | 100 |
| 5 | 10 | 100 |

Dari lima kali percobaan, hasil `processed_count` selalu berada di angka 10,
sedangkan jumlah pesanan yang seharusnya berhasil diproses adalah 100.
Program juga menampilkan pesan `RACE CONDITION TERDETEKSI`.

Race condition terjadi karena beberapa thread mengakses dan mengubah
`processed_count` secara bersamaan tanpa mekanisme sinkronisasi. Ketika
beberapa thread membaca nilai counter pada waktu yang hampir bersamaan,
mereka dapat memperoleh nilai yang sama. Setelah itu masing-masing thread
menambahkan 1 dan menuliskan hasilnya kembali. Pembaruan dari thread lain
yang terjadi sebelumnya dapat tertimpa, sehingga beberapa proses increment
tidak tercatat pada counter akhir.

Contohnya, apabila dua thread sama-sama membaca nilai `processed_count`
sebesar 5, keduanya dapat menghitung nilai berikutnya sebagai 6. Walaupun
dua pesanan sudah diproses, counter hanya menjadi 6, bukan 7. Kejadian
seperti ini menyebabkan nilai akhir counter lebih kecil daripada jumlah
pesanan yang sebenarnya diproses.

## Percobaan dengan Lock
Setelah percobaan tanpa `Lock`, program diperbaiki dengan menggunakan
`threading.Lock()` untuk melindungi bagian yang melakukan increment terhadap
`processed_count`.

Program kemudian dijalankan sebanyak 5 kali dengan kondisi yang sama, yaitu
100 pesanan dan 10 thread pekerja.

| Percobaan | Hasil `processed_count` | Seharusnya |
|---|---:|---:|
| 1 | 100 | 100 |
| 2 | 100 | 100 |
| 3 | 100 | 100 |
| 4 | 100 | 100 |
| 5 | 100 | 100 |

Dari lima kali percobaan, hasil `processed_count` selalu tepat 100. Pesan
yang muncul adalah `Semua pesanan berhasil diproses dengan Lock.`

Penggunaan `Lock` membuat bagian increment `processed_count` hanya dapat
dijalankan oleh satu thread pada satu waktu. Dengan demikian, thread lain
harus menunggu sampai thread yang sedang mengubah counter selesai. Setelah
itu thread berikutnya dapat melakukan increment menggunakan nilai counter
yang sudah diperbarui.

Berdasarkan hasil percobaan, penggunaan `Lock` berhasil mencegah kehilangan
increment yang terjadi pada percobaan tanpa `Lock`, sehingga nilai akhir
`processed_count` sesuai dengan jumlah pesanan, yaitu 100.

## Analisis: Mengapa Menggunakan Threading?

Pada kasus FoodGo, masalahnya adalah setiap pesanan diproses menggunakan
proses baru. Kalau pesanan yang masuk sedikit mungkin tidak terlalu terasa,
tetapi kalau ada banyak pesanan yang masuk secara bersamaan, penggunaan
resource komputer bisa menjadi lebih besar karena setiap proses mempunyai
overhead sendiri.

Karena itu, pada tugas ini digunakan multithreading. Dengan threading,
beberapa pesanan bisa diproses secara konkuren menggunakan beberapa thread
dalam satu proses. Pada program ini digunakan 10 thread untuk memproses 100
pesanan.

Penggunaan thread lebih sesuai dengan kasus ini karena tidak perlu membuat
proses OS baru untuk setiap pesanan. Jadi, dibandingkan membuat 100 proses
untuk 100 pesanan, pekerjaan dapat dibagi ke beberapa thread yang bekerja
dalam proses yang sama.

Walaupun begitu, penggunaan beberapa thread juga menimbulkan masalah ketika
beberapa thread mengakses data yang sama. Pada program ini data yang digunakan
bersama adalah `processed_count`. Hal ini terbukti pada percobaan tanpa Lock,
di mana hasil akhirnya hanya 10 dari 100 pesanan karena terjadi race condition.

Untuk mengatasi masalah tersebut digunakan `threading.Lock()`. Dengan Lock,
hanya satu thread yang dapat melakukan perubahan pada `processed_count` pada
satu waktu. Setelah menggunakan Lock, hasil percobaan menjadi 100 dari 100
pesanan.

Jadi, threading digunakan agar beberapa pesanan dapat diproses secara
konkuren tanpa harus membuat proses baru untuk setiap pesanan, sedangkan
Lock digunakan untuk menjaga agar data yang digunakan bersama tetap aman.

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 04-10-2026 | ChatGPT | Meminta penjelasan singkat mengenai race condition dan Lock pada multithreading | Memberikan penjelasan umum tentang race condition dan fungsi Lock | Digunakan sebagai referensi untuk memahami konsep, kemudian hasil percobaan program digunakan sebagai dasar penulisan jurnal |
| 04-10-2026 | ChatGPT | Meminta arahan umum mengenai cara menjalankan program Python untuk pengujian | Memberikan arahan mengenai menjalankan program melalui terminal dan membandingkan hasil pengujian | Pengujian dan pengambilan hasil dilakukan sendiri melalui terminal |
