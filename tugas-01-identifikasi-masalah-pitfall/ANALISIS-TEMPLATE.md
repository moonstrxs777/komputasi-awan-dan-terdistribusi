# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Aziz Faadihillah | 103072400103 | [pitfall/bagian yang dikerjakan] |
| Riandhika Bagus Rosdyantoro | 103072400088 | [pitfall/bagian yang dikerjakan] |
| Muhammad Naufal Sniper H | 103072430003 | [pitfall 3 Single Point of Failure] |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 3: [Single Point of Failure] — ditulis oleh [Muhammad Naufal Sniper Hazza Athallah]

**Bukti di skenario:** FoodGo menggunakan satu server yang menangani semua modul, yaitu pesanan, pembayaran, dan notifikasi kurir, dalam satu proses monolitik. Saat trafik meningkat, server tersebut menjadi kewalahan

**Kenapa ini keliru:** Arsitektur yang menempatkan banyak fungsi penting pada satu server membuat sistem sulit menangani peningkatan beban secara fleksibel. Beban tinggi pada satu fungsi dapat ikut memengaruhi fungsi lainnya. Selain itu, server tersebut menjadi titik kegagalan karena jika mengalami crash, beberapa layanan FoodGo dapat terganggu secara bersamaan.

**Dampak ke FoodGo:** Ketika jumlah pesanan meningkat, server harus memproses pesanan, pembayaran, dan notifikasi secara bersamaan. Resource seperti CPU, memori, dan koneksi dapat habis sehingga aplikasi menjadi lambat dan beberapa request mengalami timeout. Jika server akhirnya crash, seluruh modul yang berjalan pada server tersebut ikut berhenti dan membutuhkan restart manual.

**Solusi desain awal:** Memisahkan modul utama menjadi beberapa service yang dapat berjalan secara terpisah, misalnya Order Service, Payment Service, dan Notification Service. Service yang menerima beban lebih tinggi dapat diberi resource atau instance tambahan secara independen. Selain itu, dapat diterapkan load balancing untuk membagi request ke beberapa instance.

**Trade-off:** Pemisahan service membuat sistem lebih kompleks karena komunikasi antar-service harus dikelola dengan baik. Tim juga perlu menangani masalah seperti monitoring, konfigurasi, dan kegagalan komunikasi antar-service yang sebelumnya lebih sederhana pada sistem monolitik.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
