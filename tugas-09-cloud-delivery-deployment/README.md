# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

### 1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.

Rekomendasi deployment model yang paling cocok adalah hybrid cloud jika melihat kebutuhan sistem. Hybrid cloud merupakan gabungan dari private cloud dan public cloud untuk mendukung kebutuhan sistem, karena kebutuhan utama adalah menjaga kerahasiaan data dan menyediakan layanan untuk melayani ribuan instansi dengan pola akses tidak merata maka model ini dapat digunakan. Private Cloud digunakan untuk menyimpan dan memproses data sensitif, seperti nama, NIK, alamat, dan data biometrik, sehingga tetap berada dalam infrastruktur yang dikendalikan pemerintah. Sedangkan public cloud digunakan untuk layanan pendukung yang tidak menyimpan atau memproses data pribadi, seperti website informasi publik dan distribusi konten. Kami menggunakan asumsi bahwa larangan penempatan data pada infrastruktur yang tidak sepenuhnya dikendalikan oleh negara berlaku terhadap data pribadi penduduk. Dengan demikian, komponen sistem yang tidak menyimpan atau memproses data pribadi mentah diperbolehkan menggunakan Public Cloud, sedangkan seluruh data pribadi dan proses verifikasi identitas tetap berada di Private Cloud milik pemerintah.

Berikut analisis berdasarkan 5 karakteristik NIST:

a. on demand self service: Administrator dapat menyediakan sumber daya komputasi secara mandiri sesuai kebutuhan, contohnya menambah kapasitas server ketika terjadi peningkatan akses menjelang pemilu atau pendaftaran sekolah.

b. broad network access: Sistem dapat diakses melalui jaringan aman oleh ribuan instansi, seperti Dukcapil daerah, kepolisian, dan perbankan, sesuai hak akses masing-masing.

c. resource pooling: karakteristik sumber daya komputasi (server, penyimpanan, jaringan) dikumpulkan sehingga bisa digunakan bersama beberapa user. Private cloud sendiri melayani pemrosesan data kependudukan sedangkan public cloud melayani komponen pendukung non sensitif.

d. rapid elasticity: emampuan sumber daya komputasi untuk bertambah atau berkurang secara cepat sesuai dengan perubahan kebutuhan penggunaan sistem. Public Cloud dapat menangani lonjakan trafik layanan informasi, sedangkan Private Cloud menerapkan horizontal scaling untuk mendukung peningkatan permintaan verifikasi data.

e. measured service: penggunaan sumber daya seperti penggunaan CPU, penyimpanan bandwidth dan jumlah permintaan layanan dapat dipantau. Sehingga dapat membntu pemerintah mengoptimalkan kapasitas dan mengawasi penggunaan sistem

Dari analisis tersebut, kami mempertimbangkan Hybrid Cloud karena mampu menggabungkan kerahasiaan Private Cloud dengan fleksibilitas Public Cloud. Data pribadi dan proses verifikasi identitas tetap berada di infrastruktur pemerintah, sedangkan layanan pendukung non-sensitif memanfaatkan Public Cloud untuk meningkatkan skalabilitas. Dengan penerapan kelima karakteristik NIST, sistem diharapkan mampu melayani ribuan instansi secara efisien tanpa mengabaikan keamanan data penduduk.

### 2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).

Untuk menentukan service model yang tepat dalam Sistem Data Kependudukan, terdapat tiga model yang dipertimbangkan, yaitu Infrastructure as a Service (IaaS), Platform as a Service (PaaS), dan Software as a Service (SaaS).

a. Infrastructure as a Service (IaaS)

IaaS menyediakan infrastruktur komputasi berupa virtual machine, jaringan, dan storage. Model ini memberikan kontrol lebih besar kepada pemerintah untuk mengelola sistem operasi, konfigurasi jaringan, penyimpanan, serta aplikasi yang digunakan. Hal ini menjadi pertimbangan penting karena sistem menyimpan data sensitif penduduk, seperti nama, NIK, alamat, dan data biometrik. Selain itu, kapasitas infrastruktur dapat ditingkatkan sesuai kebutuhan ketika terjadi lonjakan akses.

b. Platform as a Service (PaaS)

PaaS menyediakan platform untuk menjalankan dan mengembangkan aplikasi tanpa harus mengelola server, sistem operasi, maupun infrastruktur di bawahnya. Model ini cocok untuk pengembangan aplikasi dan API verifikasi identitas karena tim pengembang dapat lebih fokus pada kode aplikasi. Namun, kontrol pemerintah terhadap infrastruktur dan sistem operasi lebih terbatas dibandingkan IaaS.

c. Software as a Service (SaaS)

SaaS menyediakan aplikasi siap pakai yang dapat langsung digunakan melalui browser atau API tanpa perlu mengelola infrastruktur maupun platform. Model ini cocok untuk kebutuhan umum seperti email kedinasan, pengelolaan dokumen, dan kolaborasi internal. Namun, SaaS kurang sesuai untuk menjadi model utama Sistem Data Kependudukan karena pemerintah memiliki keterbatasan dalam mengendalikan pengelolaan aplikasi dan infrastruktur yang disediakan provider.

Berdasarkan analisis terhadap ketiga service model tersebut, kelompok kami merekomendasikan penggunaan kombinasi IaaS, PaaS, dan SaaS untuk komponen Sistem Data Kependudukan. Pemilihan service model disesuaikan dengan kebutuhan masing-masing komponen, terutama dari segi keamanan data, kontrol infrastruktur, serta kemudahan pengembangan dan pengelolaan sistem. Adapun pembagian service model untuk setiap komponen dapat dilihat pada tabel berikut.

| No. | Komponen Sistem | Service Model | Alasan Pemilihan |
|---|---|---|---|
| 1 | Database inti kependudukan (NIK, nama, alamat, dan data biometrik) | **IaaS** | Membutuhkan kontrol lebih besar terhadap sistem operasi, konfigurasi jaringan, penyimpanan, dan pengaturan keamanan karena menyimpan data pribadi yang sensitif. |
| 2 | Mesin pencocokan biometrik | **IaaS** | Membutuhkan kapasitas komputasi yang besar dan pengaturan keamanan khusus untuk memproses data biometrik. IaaS memberikan keleluasaan untuk mengatur sumber daya server dan jaringan sesuai kebutuhan sistem.|
| 3 | Backend dan API verifikasi identitas | **PaaS** | Memudahkan pengembangan dan pengelolaan aplikasi tanpa harus mengelola server serta sistem operasi secara langsung. Tim pengembang dapat lebih fokus pada pengembangan kode aplikasi. |
| 4 | Portal publik untuk pengecekan status layanan | **PaaS** | Memudahkan pengembangan dan pemeliharaan portal serta mendukung penyesuaian kapasitas ketika terjadi peningkatan jumlah pengunjung. |
| 5 | Email kedinasan dan pengelolaan dokumen internal | **SaaS** | Menyediakan aplikasi siap pakai untuk kebutuhan komunikasi dan kolaborasi internal sehingga pemerintah tidak perlu membangun dan mengelola aplikasi tersebut sendiri. |


### 3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).

a. Risiko kebocoran data melalui batas antara Private Cloud dan Public Cloud

Portal publik dan CDN berada di Public Cloud yang terhubung ke internet, sehingga bisa menjadi pintu masuk serangan (misalnya SQL injection, penyalahgunaan API, atau pencurian kredensial) menuju layanan di Private Cloud. Jika batas keduanya lemah, data pribadi penduduk yang seharusnya tertutup bisa terekspos.

Mitigasi:

- Menerapkan segmentasi jaringan (DMZ) dan prinsip zero trust antara kedua segmen.
- Menggunakan mTLS, API gateway, rate limiting, dan WAF pada jalur komunikasi.
- Membatasi data yang keluar ke Public Cloud. Portal publik hanya menerima status atau hasil verifikasi (misalnya "terdaftar" atau "tidak terdaftar") dan tidak - -pernah menerima data pribadi mentah.
- Mengenkripsi data saat disimpan dan saat dikirim, dengan kunci enkripsi dikelola di dalam Private Cloud.

b. Risiko sinkronisasi data antara Private Cloud dan Public Cloud

Portal publik menampilkan status layanan berdasarkan data yang bersumber dari Private Cloud. Jika data di sisi publik terlambat diperbarui, warga bisa melihat status yang sudah tidak sesuai. Komunikasi antar segmen juga menambah latensi.

Mitigasi:

- Menetapkan Private Cloud sebagai sumber data utama (single source of truth). Public Cloud hanya menyimpan salinan sementara (cache) untuk data non-sensitif.
- Menggunakan masa berlaku cache yang singkat dan pembaruan otomatis ketika data berubah.
- Memantau keterlambatan replikasi dan menguji beban sebelum musim puncak.

c. Risiko keterbatasan kapasitas Private Cloud saat lonjakan verifikasi

Sesuai nomor 2, backend dan API verifikasi identitas serta mesin pencocokan biometrik berada di Private Cloud. Saat pemilu atau pendaftaran sekolah, jumlah permintaan verifikasi dari ribuan instansi melonjak, sedangkan kapasitas Private Cloud dibatasi oleh perangkat fisik yang tersedia sehingga bisa terjadi antrean atau downtime.

Mitigasi:

- Menerapkan horizontal scaling pada Private Cloud dan menyiapkan cadangan kapasitas berdasarkan perkiraan beban puncak (capacity planning).
- Menggunakan cache hasil verifikasi, antrean permintaan, dan pembatasan kuota per instansi agar beban terkendali.
- Memindahkan beban non-sensitif ke Public Cloud supaya sumber daya Private Cloud fokus pada verifikasi.
- Melakukan uji beban secara berkala dengan simulasi lonjakan akses.

### 4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
