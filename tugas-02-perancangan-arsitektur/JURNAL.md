# Jurnal Proses — Tugas 2

24 September 2026
- Arsitektur yang digunakan: Kombinasi Service-Oriented Architecture (SOA) + Publish-Subscribe
- Alasan pemilihan: SOA digunakan untuk memisahkan sistem FoodGo menjadi beberapa service berdasarkan fungsi, yaitu Order Service, Payment Service, Restaurant Catalog Service, dan Courier/Notification Service. Publish-Subscribe digunakan untuk komunikasi berbasis event melalui Message Broker. Kombinasi keduanya dipilih untuk mengurangi coupling antar modul dan memungkinkan setiap service dikembangkan serta di-deploy secara lebih independen.
- Komponen yang digunakan: API Gateway sebagai pintu masuk request, Order Service untuk mengelola pesanan, Payment Service untuk memproses pembayaran, Restaurant Catalog Service untuk mengelola data restoran dan menu, Courier/Notification Service untuk penugasan kurir dan notifikasi, serta Message Broker sebagai perantara komunikasi berbasis event.
- Alur komunikasi: Komunikasi sinkron request-response digunakan pada proses pelanggan ke API Gateway, Order Service dengan Restaurant Catalog Service, dan Order Service dengan Payment Service. Komunikasi asinkron berbasis event digunakan melalui Message Broker menggunakan event OrderPaid dan CourierAssigned.
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): Pada versi 2, alur komunikasi antar-service diperjelas dengan membedakan komunikasi sinkron request-response dan komunikasi asinkron publish-subscribe. Message Broker digunakan sebagai perantara event OrderPaid dan CourierAssigned. Perubahan ini dilakukan agar interaksi antar-service lebih jelas dan menunjukkan penerapan SOA + Publish-Subscribe pada kasus FoodGo.
- Analisis coupling: SOA digunakan untuk memisahkan modul FoodGo menjadi beberapa service, sedangkan Publish-Subscribe digunakan untuk mengurangi ketergantungan langsung antar-service. Arsitektur juga menerapkan timeout dan retry untuk menangani latency dan kegagalan jaringan serta pemisahan service untuk mengurangi dampak Single Point of Failure.
- Trade-off: Penerapan SOA + Publish-Subscribe meningkatkan kompleksitas sistem karena terdapat beberapa service dan Message Broker. Selain itu, debugging dan monitoring menjadi lebih sulit, retry dapat menambah beban sistem, dan konsistensi data menjadi lebih kompleks karena komunikasi asinkron dapat menyebabkan jeda dalam pemrosesan event.

27 September 2026
- Melakukan pengecekan dan perapian kembali isi Tugas 2 agar sesuai dengan instruksi dan rubrik.
- Memastikan diagram, alur komunikasi, analisis coupling, dan trade-off sudah konsisten dengan arsitektur SOA + Publish-Subscribe.
- Melakukan revisi akhir dan mem-*fix* tugas agar siap dikumpulkan.

## Log Penggunaan AI (Level 2)

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 24 September 2026 | ChatGPT | Bantu menentukan komponen yang umum digunakan pada arsitektur SOA dan Publish-Subscribe untuk kasus FoodGo. | Memberikan ide komponen seperti API Gateway, Order Service, Payment Service, Restaurant Catalog Service, Courier/Notification Service, dan Message Broker. | Ide tersebut digunakan sebagai bahan brainstorming, kemudian kelompok menyesuaikan komponen dengan kebutuhan dan studi kasus FoodGo. |
| 24 September 2026 | ChatGPT | Bantu menentukan jenis komunikasi yang dapat digunakan antar-service pada FoodGo. | Memberikan ide penggunaan komunikasi sinkron request-response untuk proses yang membutuhkan respons langsung dan komunikasi asinkron berbasis event melalui Message Broker. | Ide tersebut digunakan sebagai referensi, kemudian kelompok menentukan penggunaan komunikasi sinkron dan asinkron berdasarkan alur sistem yang dirancang. |
| 24 September 2026 | ChatGPT | Bantu menentukan contoh event yang sesuai untuk komunikasi Publish-Subscribe pada FoodGo. | Memberikan ide penggunaan event seperti `OrderPaid` dan `CourierAssigned` untuk menggambarkan komunikasi berbasis event. | Event digunakan sebagai bahan brainstorming dan disesuaikan dengan alur pembayaran, penugasan kurir, dan pembaruan status pesanan pada rancangan kelompok. |
| 24 September 2026 | ChatGPT | Bantu mengidentifikasi hal yang perlu diperhatikan dalam penerapan SOA + Publish-Subscribe pada FoodGo. | Memberikan ide mengenai timeout, retry, Message Broker, debugging, monitoring, dan konsistensi data sebagai hal yang perlu diperhatikan. | Ide tersebut digunakan sebagai bahan diskusi kelompok, kemudian trade-off dan hubungan dengan pitfall Tugas 1 disusun berdasarkan rancangan dan pemahaman kelompok. |
