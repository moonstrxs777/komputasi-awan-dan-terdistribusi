# Jurnal Proses — Tugas 9

## Diskusi deployment model
Opsi yang dipertimbangkan dan kenapa akhirnya memilih salah satu: 

Dalam menentukan deployment model untuk Sistem Data Kependudukan, kelompok kami mempertimbangkan empat opsi, yaitu Public Cloud, Private Cloud, Community Cloud, dan Hybrid Cloud. Public Cloud menawarkan fleksibilitas dan skalabilitas yang tinggi, tetapi kurang sesuai untuk menyimpan data kependudukan yang bersifat rahasia karena infrastrukturnya dikelola oleh penyedia layanan. Private Cloud memberikan kontrol dan keamanan yang lebih besar karena infrastrukturnya dapat dikelola langsung oleh pemerintah, tetapi membutuhkan pengelolaan kapasitas agar mampu menangani lonjakan akses. Sementara itu, Community Cloud memungkinkan beberapa organisasi menggunakan infrastruktur bersama, tetapi membutuhkan pengaturan pengelolaan dan tanggung jawab antarorganisasi yang lebih kompleks.

Berdasarkan pertimbangan tersebut, kelompok kami memilih Hybrid Cloud, yaitu kombinasi antara Private Cloud dan Public Cloud. Private Cloud digunakan untuk menyimpan dan memproses data pribadi penduduk, termasuk nama, NIK, alamat, dan data biometrik, serta menjalankan proses verifikasi identitas. Sementara itu, Public Cloud digunakan untuk layanan pendukung yang tidak menyimpan atau memproses data pribadi, seperti website informasi publik dan distribusi konten. Pemilihan Hybrid Cloud didasarkan pada kebutuhan untuk menjaga kerahasiaan data sekaligus menyediakan fleksibilitas dalam menangani peningkatan jumlah akses. Dengan demikian, data pribadi tetap berada dalam infrastruktur yang dikendalikan pemerintah, sedangkan layanan non-sensitif dapat memanfaatkan skalabilitas Public Cloud.

## Diskusi service model per komponen
Dalam menentukan service model, kelompok kami mempertimbangkan tiga pilihan, yaitu Infrastructure as a Service (IaaS), Platform as a Service (PaaS), dan Software as a Service (SaaS). Ketiganya memiliki karakteristik dan tingkat pengelolaan yang berbeda sehingga pemilihannya disesuaikan dengan kebutuhan masing-masing komponen Sistem Data Kependudukan.

IaaS dipilih untuk database inti kependudukan dan mesin pencocokan biometrik karena kedua komponen tersebut menangani data sensitif dan membutuhkan pengaturan infrastruktur yang lebih spesifik. IaaS memberikan keleluasaan kepada pemerintah untuk mengelola sistem operasi, jaringan, penyimpanan, serta kapasitas komputasi sesuai kebutuhan sistem.

PaaS digunakan untuk backend dan API verifikasi identitas serta portal publik untuk pengecekan status layanan. Model ini dipilih karena dapat mempermudah proses pengembangan dan pemeliharaan aplikasi tanpa mengharuskan tim pengembang mengelola server dan sistem operasi secara langsung. Selain itu, PaaS mendukung penyesuaian kapasitas aplikasi ketika terjadi peningkatan jumlah pengguna.

Sementara itu, SaaS digunakan untuk kebutuhan email kedinasan dan pengelolaan dokumen internal. Model ini dipilih karena menyediakan aplikasi siap pakai sehingga pemerintah tidak perlu membangun dan mengelola aplikasi pendukung tersebut secara mandiri.

Dengan demikian, kelompok kami merekomendasikan kombinasi IaaS, PaaS, dan SaaS untuk komponen yang berbeda. Kombinasi ini memungkinkan setiap komponen menggunakan layanan yang sesuai dengan kebutuhan keamanan, kontrol infrastruktur, serta kemudahan pengembangan dan pengelolaan sistem.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
