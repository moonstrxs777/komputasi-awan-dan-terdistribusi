# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [ZZEYF FAMS]

| Nama | NIM | Kontribusi |
|---|---|---|
| Aziz Faadihillah | 103072400103 | [pitfall 1 Single Point of Failure] |
| Riandhika Bagus Rosdyantoro | 103072400088 | [pitfall 2 The Network is Reliable]] |
| Muhammad Naufal Sniper H | 103072430003 | [pitfall 3 Single Point of Failure] |

## Pitfall 1: [Single Point of Failure] — ditulis oleh [Aziz Faadihilah]

**Bukti di skenario:** Di skenario dijelaskan bahwa "satu server menangani semua modul (pesanan, pembayaran, notifikasi kurir)" dan semuanya berjalan dalam satu proses monolitik yang sama. Ketika trafik naik, server tersebut kewalahan dan kadang crash sampai harus di-restart secara manual.

**Kenapa ini keliru:** FoodGo menjalankan modul pesanan, pembayaran, dan notifikasi kurir dalam satu proses pada satu server. Akibatnya, ketika server tersebut mengalami masalah, modul-modul yang berjalan di dalamnya juga ikut terdampak. Kondisi ini membuat satu server menjadi single point of failure, karena kegagalan pada server tersebut dapat mengganggu beberapa fungsi sekaligus.

**Dampak ke FoodGo:** Saat jam makan siang atau promo besar, jumlah request meningkat dan server harus menangani pesanan, pembayaran, serta notifikasi kurir secara bersamaan. Resource server akhirnya terbagi untuk semua proses tersebut. Jika server kehabisan resource atau crash, pengguna tidak hanya mengalami masalah ketika membuat pesanan, tetapi pembayaran dan notifikasi kurir juga dapat ikut berhenti. Karena server perlu di-restart secara manual, gangguan juga bisa berlangsung sampai proses restart selesai.

**Solusi desain awal:** FoodGo dapat memisahkan modul pesanan, pembayaran, dan notifikasi menjadi service yang terpisah. Setiap service dapat dijalankan secara terpisah sehingga jika salah satu service bermasalah, service lainnya masih bisa berjalan. Untuk tahap awal, FoodGo tidak harus langsung memecah seluruh aplikasi. Modul yang paling sering membebani server bisa dipisahkan terlebih dahulu, kemudian masing-masing service dapat ditambah instance ketika trafik meningkat.

**Trade-off:** Arsitektur seperti ini membutuhkan pengelolaan yang lebih rumit karena service sekarang saling berkomunikasi melalui jaringan. Tim juga harus menangani masalah seperti komunikasi yang gagal, timeout, dan monitoring tiap service. Jadi, risiko satu server mematikan seluruh sistem berkurang, tetapi pekerjaan operasional dan pengembangan menjadi lebih banyak.

---

## Pitfall 2: [The Network is Reliable] — ditulis oleh [Riandhika Bagus Rosdyantoro]

**Bukti di skenario:**
FoodGo menemukan bahwa kode mereka menulis asumsi bahwa network is always reliable dan tidak memerlukan mekanisme retry. Selain itu, pemanggilan antar-service seperti modul pesanan ke modul pembayaran tidak memiliki timeout.

**Kenapa ini keliru:**
Dalam sistem terdistribusi, jaringan tidak selalu dapat diandalkan. Komunikasi antar-service dapat mengalami gangguan, keterlambatan, kehilangan paket, atau service tujuan tidak memberikan respons. Karena itu, sistem tidak seharusnya menganggap setiap permintaan antar-service pasti berhasil.

**Dampak ke FoodGo:**
Ketika komunikasi antara modul pesanan dan pembayaran mengalami gangguan, modul pesanan dapat gagal mendapatkan respons dari modul pembayaran. Jika permintaan tetap menunggu atau tidak memiliki mekanisme penanganan kegagalan, request dapat menumpuk ketika trafik sedang tinggi. Akibatnya, resource server semakin terbebani, aplikasi menjadi lambat, beberapa permintaan mengalami timeout, dan kondisi tersebut dapat berkontribusi terhadap server mengalami crash.

**Solusi desain awal:**
FoodGo dapat menerapkan timeout dan retry dengan exponential backoff pada komunikasi antar-service. Timeout membatasi waktu tunggu ketika service tujuan tidak memberikan respons, sedangkan retry memungkinkan permintaan dicoba kembali ketika kegagalan jaringan bersifat sementara. Untuk mencegah kegagalan berantai, FoodGo juga dapat mempertimbangkan circuit breaker pada service yang sering mengalami kegagalan.

**Trade-off:**
Retry dapat menambah jumlah request ketika service tujuan sedang bermasalah. Jika dilakukan terlalu sering tanpa batas dan tanpa jeda, retry justru dapat meningkatkan beban server dan memperparah kegagalan. Karena itu, retry perlu dibatasi dan menggunakan jeda seperti exponential backoff.

## Pitfall 3: [Single Point of Failure] — ditulis oleh [Muhammad Naufal Sniper Hazza Athallah]

**Bukti di skenario:** FoodGo menggunakan satu server untuk menjalankan seluruh modul, mulai dari pesanan, pembayaran, hingga notifikasi kurir. Ketika terjadi peningkatan trafik, server tersebut menjadi kewalahan dalam menangani seluruh proses yang berjalan secara bersamaan.

**Kenapa ini keliru:** Arsitektur yang menempatkan banyak fungsi penting pada satu server membuat sistem sulit menangani peningkatan beban secara fleksibel. Beban tinggi pada satu fungsi dapat ikut memengaruhi fungsi lainnya. Selain itu, server tersebut menjadi titik kegagalan karena jika mengalami crash, beberapa layanan FoodGo dapat terganggu secara bersamaan.

**Dampak ke FoodGo:** Ketika jumlah pesanan meningkat, server harus memproses pesanan, pembayaran, dan notifikasi secara bersamaan. Resource seperti CPU, memori, dan koneksi dapat habis sehingga aplikasi menjadi lambat dan beberapa request mengalami timeout. Jika server akhirnya crash, seluruh modul yang berjalan pada server tersebut ikut berhenti dan membutuhkan restart manual.

**Solusi desain awal:** Memisahkan modul utama menjadi beberapa service yang dapat berjalan secara terpisah, misalnya Order Service, Payment Service, dan Notification Service. Service yang menerima beban lebih tinggi dapat diberi resource atau instance tambahan secara independen. Selain itu, dapat diterapkan load balancing untuk membagi request ke beberapa instance.

**Trade-off:** Pemisahan service membuat sistem lebih kompleks karena komunikasi antar-service harus dikelola dengan baik. Tim juga perlu menangani masalah seperti monitoring, konfigurasi, dan kegagalan komunikasi antar-service yang sebelumnya lebih sederhana pada sistem monolitik.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
