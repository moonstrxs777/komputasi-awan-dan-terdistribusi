# Tugas 3 (Pekan 3) — Efisiensi Proses & Kontainer

## Studi Kasus

FoodGo mengalami pemborosan sumber daya karena setiap permintaan pesanan diproses menggunakan proses baru yang memiliki overhead cukup besar. Ketika banyak pesanan masuk secara bersamaan, penggunaan memori dapat meningkat karena setiap proses memiliki resource dan overhead masing-masing.

Pada tugas ini dibuat simulasi pemrosesan pesanan menggunakan **multithreading** Python. Selain itu, dilakukan simulasi race condition pada shared counter dan diperbaiki menggunakan `threading.Lock()`. Program kemudian dikemas menggunakan Docker agar dapat dijalankan dalam container.

---

## 1. Tujuan

Tujuan dari tugas ini adalah:

1. Mengimplementasikan pemrosesan banyak pesanan secara konkuren menggunakan multithreading.
2. Memahami dan membuktikan terjadinya race condition pada shared data.
3. Menggunakan `threading.Lock()` untuk melakukan sinkronisasi antar-thread.
4. Membandingkan hasil program sebelum dan sesudah penggunaan Lock.
5. Mengemas program ke dalam Docker container.
6. Memahami hubungan antara multithreading, efisiensi resource, dan masalah pada server FoodGo.

---

## 2. Implementasi Multithreading

Program menggunakan modul `threading` dari Python untuk membuat beberapa thread yang dapat memproses pesanan secara konkuren.

Setiap thread menjalankan fungsi worker untuk memproses bagian dari pesanan. Setelah seluruh thread selesai, hasil pemrosesan dikumpulkan dan dibandingkan dengan jumlah pesanan yang seharusnya diproses.

Penggunaan multithreading dipilih karena studi kasus FoodGo membutuhkan penanganan banyak request secara bersamaan tanpa membuat proses OS baru untuk setiap request.

---

## 3. Race Condition

Race condition terjadi ketika beberapa thread mengakses dan mengubah shared data pada waktu yang hampir bersamaan. Dalam program ini, shared data berupa counter jumlah pesanan yang telah diproses.

Pada percobaan tanpa Lock, beberapa thread dapat membaca nilai counter yang sama sebelum salah satu thread menyimpan hasil perubahannya. Akibatnya, sebagian increment dapat hilang dan nilai akhir counter tidak sesuai dengan jumlah pesanan yang seharusnya diproses.

Contoh konsepnya:

```text
Thread A membaca counter
Thread B membaca counter
Thread A melakukan increment
Thread B melakukan increment
Thread A menyimpan hasil
Thread B menyimpan hasil
```

Karena adanya akses bersamaan terhadap shared counter, hasil akhirnya dapat lebih kecil dari jumlah pesanan sebenarnya.

Bukti hasil percobaan tanpa Lock dapat dilihat pada:

```text
bukti/01_race_condition.png
```

---

## 4. Perbaikan Menggunakan Lock

Race condition diperbaiki menggunakan `threading.Lock()`.

Lock digunakan untuk melindungi bagian kode yang melakukan perubahan terhadap shared counter. Dengan demikian, hanya satu thread yang dapat mengakses critical section pada satu waktu.

Walaupun terdapat Lock, seluruh program tidak berubah menjadi proses sekuensial. Thread tetap dapat menjalankan pekerjaan lainnya secara konkuren, sedangkan hanya akses terhadap shared data yang disinkronisasi.

Bukti hasil setelah menggunakan Lock dapat dilihat pada:

```text
bukti/02_with_lock.png
```

---

## 5. Perbandingan

| Kondisi     | Expected Counter |         Actual Counter | Status        |
| ----------- | ---------------: | ---------------------: | ------------- |
| Tanpa Lock  |            [isi] | [isi hasil eksperimen] | [Salah/Benar] |
| Dengan Lock |            [isi] | [isi hasil eksperimen] | [Salah/Benar] |

Berdasarkan percobaan, versi tanpa Lock dapat menghasilkan counter yang tidak sesuai karena terjadi race condition. Setelah bagian kritis dilindungi dengan Lock, hasil counter sesuai dengan jumlah pesanan yang diproses.

---

## 6. Mengapa Threading dan Bukan Multiprocessing?

Pada studi kasus FoodGo, permasalahan utama adalah penggunaan proses OS baru untuk setiap request. Pembuatan banyak proses dapat menghasilkan overhead resource yang lebih besar.

Thread berada di dalam satu proses dan dapat berbagi memory space yang sama. Oleh karena itu, penggunaan thread dapat mengurangi overhead dibandingkan membuat proses baru untuk setiap request.

Perbandingan sederhananya:

```text
Pendekatan awal FoodGo:

Request 1 → Process 1
Request 2 → Process 2
Request 3 → Process 3
...
Request 100 → Process 100

→ overhead proses meningkat
→ penggunaan memori meningkat
```

Sedangkan menggunakan multithreading:

```text
Satu proses
├── Thread 1
├── Thread 2
├── Thread 3
├── ...
└── Thread N

→ thread berbagi resource proses
→ overhead lebih kecil dibanding membuat proses OS baru
```

Namun, penggunaan threading tidak berarti selalu lebih cepat untuk semua jenis pekerjaan. Python memiliki keterbatasan tertentu pada pekerjaan CPU-bound karena Global Interpreter Lock (GIL). Untuk simulasi FoodGo pada tugas ini, threading digunakan untuk menunjukkan pemrosesan request secara konkuren dengan overhead yang lebih ringan dibandingkan membuat proses OS baru untuk setiap request.

---

## 7. Docker Container

Program kemudian dikemas menggunakan Docker agar environment eksekusinya lebih konsisten.

Proses build:

```bash
docker build -t foodgo-order-sim .
```

Setelah image berhasil dibuat, container dijalankan menggunakan:

```bash
docker run --rm foodgo-order-sim
```

Hasil eksekusi program di dalam container menunjukkan bahwa program dapat berjalan dengan fungsi yang sama seperti ketika dijalankan langsung menggunakan Python.

Bukti eksekusi Docker dapat dilihat pada:

```text
bukti/03_docker.png
```

---

## 8. Kesimpulan

Berdasarkan percobaan, multithreading dapat digunakan untuk memproses banyak pesanan secara konkuren tanpa membuat proses OS baru untuk setiap pesanan. Penggunaan shared counter juga menunjukkan bahwa akses data bersama oleh beberapa thread dapat menyebabkan race condition.

Race condition dapat diperbaiki dengan mekanisme sinkronisasi berupa `threading.Lock()`. Setelah penggunaan Lock, hasil counter menjadi sesuai dengan jumlah pesanan yang seharusnya diproses.

Docker kemudian digunakan untuk mengemas program sehingga aplikasi dapat dijalankan dalam environment container secara konsisten.
