# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.

Rekomendasi deployment model yang paling cocok adalah hybrid cloud jika melihat kebutuhan sistem. Hybrid cloaud merupakan gabungan dari private cloud dan public cloud untuk mendukung kebutuhan sistem, karena kebutuhan utama adalah menjaga kerahasiaan data dan menyediakan layanan untuk melayani ribuan instansi dengan pola akses tidak merata maka model ini dapat digunakan. Private Cloud digunakan untuk menyimpan dan memproses data sensitif, seperti nama, NIK, alamat, dan data biometrik, sehingga tetap berada dalam infrastruktur yang dikendalikan pemerintah. Sedangkan public cloud digunakan untuk layanan pendukung yang tidak menyimpan atau memproses data pribadi, seperti website informasi publik dan distribusi konten. Kami menggunakan asumsi bahwa larangan penempatan data pada infrastruktur yang tidak sepenuhnya dikendalikan oleh negara berlaku terhadap data pribadi penduduk. Dengan demikian, komponen sistem yang tidak menyimpan atau memproses data pribadi mentah diperbolehkan menggunakan Public Cloud, sedangkan seluruh data pribadi dan proses verifikasi identitas tetap berada di Private Cloud milik pemerintah.

Berikut analisis berdasarkan 5 karakteristik NIST:

a. on demand self service: Administrator dapat menyediakan sumber daya komputasi secara mandiri sesuai kebutuhan, contohnya menambah kapasitas server ketika terjadi peningkatan akses menjelang pemilu atau pendaftaran sekolah.

b. broad network access: Sistem dapat diakses melalui jaringan aman oleh ribuan instansi, seperti Dukcapil daerah, kepolisian, dan perbankan, sesuai hak akses masing-masing.

c. resource pooling: karakteristik sumber daya komputasi (server, penyimpanan, jaringan) dikumpulkan sehingga bisa digunakan bersama beberapa user. Private cloud sendiri melayani pemrosesan data kependudukan sedangkan public cloud melayani komponen pendukung non sensitif.

d. rapid elasticity: emampuan sumber daya komputasi untuk bertambah atau berkurang secara cepat sesuai dengan perubahan kebutuhan penggunaan sistem. Public Cloud dapat menangani lonjakan trafik layanan informasi, sedangkan Private Cloud menerapkan horizontal scaling untuk mendukung peningkatan permintaan verifikasi data.

e. measured service: penggunaan sumber daya seperti penggunaan CPU, penyimpanan bandwidth dan jumlah permintaan layanan dapat dipantau. Sehingga dapat membntu pemerintah mengoptimalkan kapasitas dan mengawasi penggunaan sistem

Dari analisis tersebut, kami mempertimbangkan Hybrid Cloud karreena mampu menggabungkan kerahasiaan Private Cloud dengan fleksibilitas Public Cloud. Data pribadi dan proses verifikasi identitas tetap berada di infrastruktur pemerintah, sedangkan layanan pendukung non-sensitif memanfaatkan Public Cloud untuk meningkatkan skalabilitas. Dengan penerapan kelima karakteristik NIST, sistem diharapkan mampu melayani ribuan instansi secara efisien tanpa mengabaikan keamanan data penduduk.

2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

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
