# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [ZZEYF FAMS]

| Nama | NIM | Kontribusi |
|---|---|---|
| Aziz Faadihillah | 103072400103 | [pitfall 1 Latency is zero] |
| Riandhika Bagus Rosdyantoro | 103072400088 | [pitfall 2 The Network is Reliable] |
| Muhammad Naufal Sniper H | 103072430003 | [pitfall 3 Single Point of Failure] |

## Pitfall 1: [Latency is zero] — ditulis oleh [Aziz Faadihilah]

**Bukti di skenario:** Di skenario dijelaskan bahwa tidak ada timeout pada pemanggilan antar-service. Modul pesanan memanggil modul pembayaran dan "menunggu tanpa batas waktu". Hal ini menunjukkan adanya asumsi bahwa respons dari service lain akan selalu datang tanpa keterlambatan yang perlu ditangani.

**Kenapa ini keliru:** Dalam sistem terdistribusi, komunikasi antar-service membutuhkan waktu dan respons tidak selalu datang dengan cepat. Saat service pembayaran sedang sibuk atau mengalami gangguan, modul pesanan bisa menunggu lebih lama. Karena FoodGo tidak memberikan batas waktu pada pemanggilan tersebut, proses yang menunggu dapat terus menggunakan resource server.

**Dampak ke FoodGo:** Saat trafik sedang tinggi, misalnya ketika jam makan siang atau promo besar, banyak request pesanan bisa memanggil service pembayaran secara bersamaan. Jika pembayaran lambat, request dari modul pesanan akan terus menunggu. Semakin banyak request yang tertahan, semakin banyak resource server yang digunakan. Kondisi ini dapat membuat aplikasi semakin lambat, beberapa request mengalami timeout, dan server bisa menjadi kewalahan sampai crash.

**Solusi desain awal:** FoodGo perlu memberikan timeout pada setiap pemanggilan antar-service, terutama komunikasi dari modul pesanan ke pembayaran. Jika service pembayaran tidak memberikan respons dalam waktu tertentu, modul pesanan dapat menghentikan penantian dan menangani kondisi tersebut sebagai kegagalan. Untuk gangguan yang sifatnya sementara, retry dengan backoff juga bisa digunakan dengan jumlah percobaan yang dibatasi.

**Trade-off:** Timeout membuat resource tidak tertahan terlalu lama, tetapi ada kemungkinan request dihentikan ketika service pembayaran sebenarnya masih bisa memberikan respons beberapa saat kemudian. Retry juga menambah request baru sehingga jika service pembayaran sedang overload, penggunaan retry yang berlebihan justru dapat menambah beban.

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
