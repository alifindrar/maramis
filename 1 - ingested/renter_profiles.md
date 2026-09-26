# Profil Pemangku Kepentingan & Direktori Penyewa Gedung A.A. Maramis (2025–2026)
## Analisis Profiling Entitas Penyewa, Kategorisasi Pemangku Kepentingan, dan Penjabaran Kategori Kegiatan

> **Dokumen Terkait:** [events_database.md](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events_database.md) | [data_analysis.md](file:///g:/My%20Drive/ANTIGRAVITY/maramis/2%20-%20analysis/data_analysis.md) | [skeleton.md](file:///g:/My%20Drive/ANTIGRAVITY/maramis/skeleton.md)  
> **Sumber Data Primer:** Teamup Calendar Pemanfaatan Gedung A.A. Maramis (172 transaksi, 254 hari okupansi)  
> **Tanggal Cut-off Data:** 26 September 2026 (Mencakup data historis terlaksana dan pipeline terjadwal s.d. Desember 2026)  
> **Kategori Kegiatan:** Mengacu secara langsung pada klasifikasi **`## 2. Event Category Breakdown`** pada basis data utama.

---

## 1. Ringkasan Eksekutif & Statistik Kilat (Quick Statistics)

Berdasarkan hasil analisis menyeluruh terhadap seluruh rekaman pemesanan (*booking transactions*) Gedung A.A. Maramis selama periode September 2025 hingga Desember 2026, teridentifikasi sebanyak **58 penyelenggara unik resmi** pada kalender sistem, serta **2 jenama komersial mandiri** yang teridentifikasi dari catatan teknis, menghasilkan total **60 entitas pemanfaat gedung**.

### 1.1. Metrik Kunci Portofolio Pemanfaatan

| Indikator Metrik | Nilai Realisasi | Keterangan & Catatan Analitis |
| :--- | :---: | :--- |
| **Total Entitas / Pihak Unik** | **60 Entitas** | 58 terdaftar langsung + 2 teridentifikasi dari entri teknis (BaTii, Kakena) |
| **Total Transaksi Kalender** | **172 Entri** | Seluruh pemesanan tercatat (2025: 58 entri, 2026: 114 entri) |
| **Kegiatan Inti (*Core Events*)** | **133 Kegiatan (77,3%)** | Acara substansial di luar sesi persiapan teknis |
| **Sesi Persiapan Teknis (*Loading & Setup*)** | **39 Kegiatan (22,7%)** | Alokasi waktu persiapan tata panggung, pencahayaan, dan dekorasi |
| **Total Hari Okupansi Gedung** | **254 Hari-Kegiatan** | 209 hari kegiatan inti + 45 hari persiapan (*loading*) |
| **Hari Kalender Unik Terisi** | **204 Hari** | Hari aktual terpakai (mengeliminasi tumpang tindih multi-ruang) |
| **Tingkat Okupansi 12 Bulan Terakhir** | **41,8%** | 153 dari 366 hari terisi (26 Sep 2025 – 26 Sep 2026) |
| **Rasio Penyelenggara Berulang (*Repeat Organizers*)** | **32,8%** | 19 entitas menyewa ≥2 kali dan menyumbang **69,4%** total kegiatan |

### 1.2. Distribusi Portofolio Berdasarkan Kategori Klien (*Client Category*)

Seluruh pihak yang telah memanfaatkan Gedung A.A. Maramis diklasifikasikan ke dalam 6 kategori utama (ditambah 1 kategori penunjang operasional fasilitas). Klasifikasi ini memperlihatkan proporsi entitas, volume kegiatan, serta durasi keterisian hari:

| Kategori Klien (*Client Category*) | Jumlah Entitas | % Entitas | Total Kegiatan | % Kegiatan | Hari Okupansi | % Hari Okupansi | Kegiatan Inti | Sesi Loading |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Government (Pemerintah & Lembaga Negara)** | 20 | 33,3% | 84 | 48,8% | 98 | 38,6% | 68 | 16 |
| **Private Entity (Korporasi Swasta, Brand & PH)** | 13 | 21,7% | 17 | 9,9% | 32 | 12,6% | 14 | 3 |
| **Public Entity (Asosiasi, Pendidikan & Festival)** | 11 | 18,3% | 27 | 15,7% | 73 | 28,7% | 21 | 6 |
| **Community (Komunitas Heritage & Publik)** | 8 | 13,3% | 17 | 9,9% | 18 | 7,1% | 17 | 0 |
| **State-Owned Enterprise (BUMN & Lembaga Keuangan)** | 4 | 6,7% | 4 | 2,3% | 5 | 2,0% | 4 | 0 |
| **Individual (Desainer & Kurator Mandiri)** | 2 | 3,3% | 2 | 1,2% | 5 | 2,0% | 2 | 0 |
| **Operational / Facility Management (Teknis Internal)** | 2 | 3,3% | 21 | 12,2% | 23 | 9,1% | 7 | 14 |
| **TOTAL KESELURUHAN** | **60** | **100,0%** | **172** | **100,0%** | **254** | **100,0%** | **133** | **39** |

### 1.3. Matriks Silang: Kategori Klien vs Kategori Kegiatan (`## 2. Event Category Breakdown`)

Matriks silang berikut memetakan secara presisi bagaimana masing-masing kategori klien memanfaatkan Gedung A.A. Maramis berdasarkan 10 kategori kegiatan yang telah distandarisasi pada dokumen acuan kalender:

| Kategori Kegiatan (`Event Category Breakdown`) | Government | BUMN | Private Entity | Public Entity | Community | Individual | Operasional | Total Acara | Total Hari |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Loading & Technical Setup** | 16 | 0 | 3 | 6 | 0 | 0 | 14 | **39** | **45** |
| **Official Meeting, Ceremony & Gala** | 26 | 2 | 1 | 1 | 0 | 0 | 2 | **32** | **36** |
| **Heritage Walking Tour & Visit** | 5 | 0 | 1 | 3 | 15 | 0 | 1 | **25** | **25** |
| **Corporate & Institutional Event** | 15 | 2 | 2 | 1 | 1 | 0 | 1 | **22** | **22** |
| **Forum, Seminar & Workshop** | 16 | 0 | 0 | 1 | 0 | 0 | 1 | **18** | **30** |
| **Photoshoot & Fashion Show** | 5 | 0 | 6 | 0 | 0 | 1 | 1 | **13** | **13** |
| **Concert & Music Performance** | 0 | 0 | 0 | 9 | 0 | 0 | 0 | **9** | **9** |
| **Exhibition, Bazaar & Festival** | 1 | 0 | 0 | 5 | 1 | 1 | 0 | **8** | **56** |
| **Film & Media Production** | 0 | 0 | 3 | 0 | 0 | 0 | 2 | **5** | **16** |
| **Maintenance & Facility Closure** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** | **2** |
| **TOTAL KEGIATAN** | **84** | **4** | **16** | **26** | **17** | **2** | **23** | **172** | **254** |

### 1.4. Daftar 15 Penyelenggara Berulang Terbesar (*Top 15 Repeat Renters*)

| Peringkat | Nama Penyelenggara / Penyewa | Kategori Klien | Sektor Asal | Total Kegiatan | Hari Okupansi | Kategori Acara Dominan |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| 1 | **Direktorat Jenderal Kekayaan Negara (DJKN)** | Government | Kemenkeu RI (Internal) | 15 | 25 | Rapimtas, Workshop, Ujian Sertifikasi |
| 2 | **Kementerian Koordinator Bidang Perekonomian** | Government | K/L Negara | 13 | 13 | Rapat Tingkat Menteri, Roundtable, Gathering |
| 3 | **Gitanada School of Music** | Public Entity | Pendidikan & Seni Musik | 11 | 11 | Konser & Resital Musik Piano Klasik |
| 4 | **Eat, Chat, Walk (ECW)** | Community | Komunitas Heritage | 10 | 10 | Walking Tour Edukasi Sejarah Arsitektur |
| 5 | **Otoritas Jasa Keuangan (OJK)** | Government | Lembaga Negara Independen | 8 | 8 | Kunjungan Tamu VVIP (Ratu Maxima), Rapat |
| 6 | **Lembaga Manajemen Aset Negara (LMAN)** | Government | BLU Kemenkeu | 8 | 8 | Stakeholders Meeting, MoU Signing, Gathering |
| 7 | **Pimpinan Kementerian Keuangan RI** | Government | Kemenkeu RI (Internal) | 8 | 8 | Upacara Hari Oeang, Jamuan Resmi Wamen |
| 8 | **Dinas Pariwisata dan Ekonomi Kreatif DKI** | Government | Pemerintah Daerah (OPD) | 4 | 4 | Koordinasi Kebijakan Pariwisata & Ekraf |
| 9 | **Biro Komunikasi & Layanan Informasi (KLI)** | Government | Kemenkeu RI (Internal) | 3 | 4 | Pelatihan Kehumasan, Fiscal Heritage Tour |
| 10 | **DJPPR Kemenkeu** | Government | Kemenkeu RI (Internal) | 3 | 3 | Rapat Pimpinan, Walking Tour Internal |
| 11 | **DJPb Kemenkeu** | Government | Kemenkeu RI (Internal) | 3 | 3 | Entry Meeting BPK, Foto Bilateral |
| 12 | **Sekretariat Jenderal Kemenkeu** | Government | Kemenkeu RI (Internal) | 3 | 3 | Pelatihan Humas, Foto Pejabat Eselon |
| 13 | **DJSPSK Kemenkeu** | Government | Kemenkeu RI (Internal) | 3 | 5 | Workshop ASEAN Audit Regulators |
| 14 | **Produksi Film Rose Pandanwangi** | Private Entity | Industri Sinema / PH | 3 | 5 | Produksi Film Biopik Sejarah |
| 15 | **Frank & Co. (PT Central Mega Kencana)** | Private Entity | Brand Perhiasan Mewah | 2 | 6 | Perayaan Ulang Tahun Mewah (Gala & Expo) |

### 1.5. Wawasan & Temuan Strategis Portofolio Klien

1. **Konsentrasi Frekuensi vs Durasi Hari:** Instansi Pemerintah mendominasi frekuensi acara (**48,8% kegiatan**), namun sebagian besar berdurasi 1 hari (rapat, workshop). Sebaliknya, segmen *Public Entity* (festival/seni) dan *Private Entity* (film/fashion/korporasi) menyumbang durasi hari yang sangat besar (**41,3% hari okupansi gabungan**), karena memerlukan waktu persiapan (*loading*) dan hari pelaksanaan pameran yang panjang (misalnya AGSI 30 hari, JICC 8 hari, Film Hatta 10 hari, Frank & Co 6 hari).
2. **Kesesuaian Tipologi Ruang:**
   - Ruang Bersejarah Utama (*Historical Halls*: Majapahit, Kutai, Bone, Sriwijaya) menjadi magnet utama bagi perhelatan prestisius kenegaraan, konser piano akustik, dan *exclusive brand activation*.
   - Gedung C Lantai 2 berfungsi sebagai 'pekerja keras' (*workhorse venue*) yang paling multifungsi dan sering disewa untuk rapat dinas, konferensi, dan gala gathering.
   - Gedung A Lantai 2 sangat diminati oleh kalangan industri kreatif untuk pameran seni rupa (AGSI), pemotretan editorial fesyen (Claude, Love & Flair), dan lokakarya.
3. **Potensi Monetisasi PNBP:** Saat ini 57% kegiatan berasal dari entitas pemerintah yang sebagian besar menggunakan mekanisme penggunaan internal kedinasan. Terdapat peluang komersialisasi masif melalui penetapan struktur tarif fleksibel untuk segmen komersial swasta, pemotretan komersial, peragaan busana, dan produksi film layar lebar yang memiliki daya bayar (*willingness to pay*) sangat tinggi.

---

## 2. Profil Penyewa: Kategori Government (Pemerintah & Lembaga Negara)

Kategori ini mencakup unit-unit kerja di lingkungan Kementerian Keuangan Republik Indonesia, kementerian koordinator, lembaga tinggi negara, otoritas independen, pemerintah daerah, serta perwakilan pemerintah asing. Karakteristik utama pemanfaatan mencakup rapat pimpinan terbatas, koordinasi lintas kementerian, pengesahan kerja sama kenegaraan, perayaan hari nasional, serta lokakarya pengembangan kapasitas pegawai.

### 2.1. Direktorat Jenderal Kekayaan Negara (DJKN)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **15 Kegiatan** | **25 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (3), Forum, Seminar & Workshop (6), Photoshoot & Fashion Show (1), Corporate & Institutional Event (2), Loading & Technical Setup (2), Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Unit Eselon I Kementerian Keuangan Republik Indonesia yang bertindak sebagai pengelola Barang Milik Negara (BMN), lelang negara, kekayaan negara dipisahkan, serta penilai aset pemerintah. DJKN merupakan pengampu utama kebijakan optimalisasi dan tata kelola aset cagar budaya Gedung A.A. Maramis.

#### B. Karakteristik Audiens & Sasaran
Pejabat tinggi Kemenkeu, pimpinan instansi pemerintah, peserta ujian sertifikasi konsultan pajak, asosiasi lelang, serta kolektor seni.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Maramis adalah representasi fisik dari BMN bernilai historis tertinggi (masterpiece heritage asset) di bawah kelolaan Kemenkeu. Digunakan untuk kegiatan berwibawa tinggi, mulai dari Rapimtas, lelang amal lukisan, hingga pusat ujian sertifikasi nasional.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-15 | **Rapat Koordinasi Kehumasan DJKN** | Official Meeting, Ceremony & Gala | Gedung A Lantai 2 | 1 hari |
| 2026-01-29 | **Kegiatan Prospera - Sekretariat DJKN** | Forum, Seminar & Workshop | Gedung A | 1 hari |
| 2026-01-30 | **Photoshoot Pejabat DJKN** | Photoshoot & Fashion Show | Gedung C | 1 hari |
| 2026-04-14 s.d. 2026-04-16 | **Ujian Sertifikasi Konsultan Pajak (DJKN) - Gd. A** | Forum, Seminar & Workshop | Gedung A | 3 hari |
| 2026-04-15 | **Sekretariat DJKN (gd C)** | Corporate & Institutional Event | Gedung C | 1 hari |
| 2026-04-19 | **Loading Rapimtas DJKN** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-04-20 | **Rapimtas DJKN** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-05-19 s.d. 2026-05-21 | **IHT Sekretariat DJKN (Gd. A)** | Forum, Seminar & Workshop | Gedung A | 3 hari |
| 2026-06-25 s.d. 2026-06-27 | **Pameran dan Lelang Lukisan - Dit. Lelang DJKN** | Exhibition, Bazaar & Festival | Gedung C Lantai 2 | 3 hari |
| 2026-07-07 s.d. 2026-07-09 | **Pelatihan K3 Sekretariat DJKN (A3)** | Forum, Seminar & Workshop | Gedung A Lantai 3 | 3 hari |
| 2026-07-15 | **FGD Risiko Iklim - DJKN (C2)** | Forum, Seminar & Workshop | Gedung C Lantai 2 | 1 hari |
| 2026-07-19 | **Loading Rapimtas DJKN (Gd. C)** | Loading & Technical Setup | Gedung C | 1 hari |
| 2026-07-20 | **Rapimtas DJKN (Gd. C)** | Official Meeting, Ceremony & Gala | Gedung C | 1 hari |
| 2026-07-28 s.d. 2026-07-30 | **Transfer Knowledge dan Ujicoba Pengembangan Modul CoreAPBN - DJKN (Gd. A2)** | Forum, Seminar & Workshop | Gedung A Lantai 2 | 3 hari |
| 2026-09-08 | **Forinves ID (DJKN Gd.C)** | Corporate & Institutional Event | Gedung C | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa internal paling dominan (15 pemesanan, 25 hari okupansi). Menjadi jangkar utama aktivitas kedinasan Kemenkeu dan etalase optimalisasi BMN cagar budaya.

---

### 2.2. Kementerian Koordinator Bidang Perekonomian (Kemenko Perekonomian)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian & Lembaga Negara
> **Statistik Sewa:** **13 Kegiatan** | **13 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (6), Forum, Seminar & Workshop (1), Corporate & Institutional Event (4), Loading & Technical Setup (2)

#### A. Profil Singkat & Latar Belakang
Kementerian koordinator yang memimpin, mengoordinasikan, dan menyinkronkan kebijakan di bidang ekonomi nasional di bawah Presiden. Kantor utamanya berlokasi di kawasan Lapangan Banteng, bersebelahan langsung dengan kompleks Maramis.

#### B. Karakteristik Audiens & Sasaran
Menteri Koordinator, Menteri teknis bidang ekonomi, pejabat Eselon I & II K/L, mitra pembangunan global, perwakilan kedutaan besar, dan akademisi ekonomi.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Kedekatan geografis yang sangat strategis (adjacent neighbor) serta kebutuhan ruang sidang formal yang representatif dan megah untuk pertemuan bilateral, rapat koordinasi tingkat menteri/Eselon I, dan konferensi meja bundar.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-01 | **Pengarahan P3K Kemenko** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 (C.2.12) | 1 hari |
| 2025-11-21 | **Kemenko High-level Roundtable on Livable Planet Economics-PIC Mya** | Forum, Seminar & Workshop | Gedung A Lantai 2 | 1 hari |
| 2025-11-24 | **Orientasi Magang Kemenko Perekonomian** | Official Meeting, Ceremony & Gala | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |
| 2025-11-28 | **kemenko 50 orang-PIC Bu Shofiah** | Corporate & Institutional Event | Gedung A Lantai 2 | 1 hari |
| 2025-12-09 | **Kemenko Perekonomian (PIC Charisma)** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2025-12-10 | **Loading inspektorat Kemenko 14.00** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2025-12-11 | **Inspektorat Kemenko Perekonomian** | Corporate & Institutional Event | Gedung C Lantai 2 | 1 hari |
| 2026-01-06 | **Kemenko Perekonomian - Rapat satgas p2sp tingkat eselon 1 dan menteri** | Official Meeting, Ceremony & Gala | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |
| 2026-01-08 | **Rapat Sesmenko & pejabat Es 2 Kemenko** | Official Meeting, Ceremony & Gala | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |
| 2026-01-09 | **Loading Kemenko** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-10 | **Natal Bersama Kemenko Perkonomian-PIC Eko** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |
| 2026-02-04 | **Kemenko** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-05-05 | **Agenda Kemenko Perekonomian (Gd. C)** | Official Meeting, Ceremony & Gala | Gedung C | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa eksternal pemerintah terbesar (13 pemesanan, 13 hari okupansi). Sangat potensial untuk kontrak pemanfaatan jangka panjang (standing corporate partner) untuk event kenegaraan dan koordinasi ekonomi.

---

### 2.3. Pimpinan Kementerian Keuangan RI

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **8 Kegiatan** | **8 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (5), Loading & Technical Setup (1), Forum, Seminar & Workshop (1), Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Kantor pimpinan tertinggi bendahara negara, meliputi Menteri Keuangan dan para Wakil Menteri Keuangan (Wamenkeu Suahasil Nazara, Wamenkeu Juda Agung, dkk.). Bertanggung jawab atas arah kebijakan fiskal, moneter makro, dan diplomasi keuangan Indonesia.

#### B. Karakteristik Audiens & Sasaran
Menteri Kabinet, jajaran Eselon I Kemenkeu, pimpinan lembaga negara mitra, perwakilan industri strategis nasional, dan tamu kenegaraan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Maramis memiliki signifikansi historis sebagai 'Gedung Putih Daendels' dan cikal bakal kantor Kementerian Keuangan era kemerdekaan (kantor Menteri Keuangan pertama A.A. Maramis). Sangat ideal untuk upacara simbolik kenegaraan (Hari Oeang RI), jamuan kepresidenan/menteri, serta FGD lintas kementerian.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-30 | **Alokasi Untuk Upacara Hari Oeang** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-18 | **Loading in acara Wamen** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-19 | **Rapat Pertemuan Antar Deputi dengan Wamen** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-02-12 | **FGD Sinkronisasi Kebijakan Industri Baja bersama Kemenperin & Kemendag** | Forum, Seminar & Workshop | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-01 | **Rapat Wamenkeu (R. Sriwijaya)** | Official Meeting, Ceremony & Gala | Gedung Utama (Historical Halls) (Ruang Sriwijaya) | 1 hari |
| 2026-07-07 | **Agenda Wamenkeu Suahasil** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-07 | **Acara Wamen Juda Agung (Gd C)** | Corporate & Institutional Event | Gedung C | 1 hari |
| 2026-10-30 | **Hari Oeang** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa berulang prestisius (8 kegiatan, 8 hari). Menetapkan standar wibawa gedung bagi publik dan memperkuat identitas Maramis sebagai 'The Financial Heritage Landmark of Indonesia'.

---

### 2.4. Otoritas Jasa Keuangan (OJK)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Lembaga Negara Independen / Pengawas Jasa Keuangan
> **Statistik Sewa:** **8 Kegiatan** | **8 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (2), Forum, Seminar & Workshop (2), Loading & Technical Setup (3), Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Lembaga negara independen yang bertugas mengatur, mengawasi, memeriksa, dan menyidik sektor jasa perbankan, pasar modal, perasuransian, dana pensiun, dan lembaga pembiayaan. Kantor pusat OJK berjarak sangat dekat di kawasan Lapangan Banteng / Soemitro Djojohadikusumo.

#### B. Karakteristik Audiens & Sasaran
Dewan Komisioner OJK, pimpinan industri perbankan & pasar modal, asosiasi kepatuhan GRC, duta besar, serta delegasi internasional (termasuk HM Ratu Máxima dari Belanda).

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memerlukan lokasi prestige untuk menerima tamu kehormatan internasional tingkat kepala negara/monarki serta menyelenggarakan konferensi pers dan forum akbar industri keuangan nasional.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-27 | **Menyambut HM Queen Maxima (Ratu Belanda) oleh DLIK OJK** | Corporate & Institutional Event | Gedung C Lantai 2 | 1 hari |
| 2026-01-21 | **Konferensi Pers OJK di Gedung C (siang)** | Forum, Seminar & Workshop | Gedung C | 1 hari |
| 2026-02-02 | **Loading in acara OJK** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-02-03 | **Agenda OJK** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-04-06 | **Loading acara OJK** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-04-07 | **OJK - Forum GRC Road to RGS 2026 : Halal Bihalal bersama Aspsiasi Profesi GRC** | Forum, Seminar & Workshop | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-09 | **Loading OJK** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-10 | **OJK** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa berulang tingkat tinggi (8 pemesanan, 8 hari). Mitra strategis utama dari sektor regulator keuangan untuk pemesanan rutin forum kepatuhan, konpres kuartalan, dan simposium keuangan berkelanjutan.

---

### 2.5. Lembaga Manajemen Aset Negara (LMAN)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Badan Layanan Umum (BLU) Kementerian Keuangan RI
> **Statistik Sewa:** **8 Kegiatan** | **8 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (6), Loading & Technical Setup (1), Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Badan Layanan Umum di bawah Kemenkeu yang mengemban mandat optimalisasi aset properti negara dan pendanaan pengadaan tanah Proyek Strategis Nasional (PSN). Merupakan pionir dalam monetisasi aset cagar budaya pemerintah.

#### B. Karakteristik Audiens & Sasaran
Investor swasta, konsultan properti, jajaran Badan Pemeriksa Keuangan (BPK), kontraktor infrastruktur, jajaran pimpinan BUMN (PT MRT Jakarta, KKKS migas), dan stakeholder pengadaan lahan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menampilkan contoh nyata (showcase model) pemanfaatan aset cagar budaya bernilai tinggi kepada para investor dan mitra BUMN saat penandatanganan kerja sama strategis (PKS/MoU).

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-20 | **LMAN - Stakeholders Meeting (PET)** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 (C.2.12, C.2.3) | 1 hari |
| 2025-10-22 | **LOADING C2 LMAN Stakeholders Meeting** | Loading & Technical Setup | Gedung C Lantai 2 | 1 hari |
| 2025-10-23 | **LMAN - Stakeholders Meeting (PP2)** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |
| 2025-11-26 | **LMAN - Investor Gathering** | Corporate & Institutional Event | Gedung C Lantai 2 | 1 hari |
| 2025-12-03 | **LMAN (PDT) (Majapahit) - Rapat Koordinasi Tindak Lanjut Rekomendasi BPK** | Official Meeting, Ceremony & Gala | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |
| 2025-12-16 | **Rapat LMAN dengan PKN dan PKKN** | Official Meeting, Ceremony & Gala | Gedung A Lantai 2 | 1 hari |
| 2025-12-17 | **Penandatanganan PKS LMAN dan KKKS - Penandatanganan MOU LMAN dan MRT** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-04-01 | **Malam apresiasi mitra jasa konsultasi (LMAN)** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa berulang utama (8 pemesanan, 8 hari). LMAN merupakan penggerak utama ekosistem optimalisasi aset; sangat potensial menjadi mitra kurasi tenant komersial jangka panjang Maramis.

---

### 2.6. Biro Komunikasi dan Layanan Informasi (KLI Kemenkeu)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **3 Kegiatan** | **4 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Forum, Seminar & Workshop (1), Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Unit kerja di bawah Sekretariat Jenderal Kemenkeu yang bertanggung jawab atas strategi kehumasan terpadu, komunikasi kebijakan fiskal, hubungan media massa, dan literasi publik APBN.

#### B. Karakteristik Audiens & Sasaran
Pegawai aparatur sipil negara penggiat media sosial (Employee Advocacy Champions), wartawan parlemen/ekonomi, komunitas sejarah, dan publik pemuda.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memanfaatkan nilai historis dan estetika arsitektur Maramis sebagai materi konten komunikasi visual, pelatihan kehumasan internal, dan tur literasi sejarah fiskal (Fiscal Heritage Explorer).

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-27 | **LOADING C2 Biro KLI** | Loading & Technical Setup | Gedung C Lantai 2 | 1 hari |
| 2025-10-28 s.d. 2025-10-29 | **IHT for Employee Advocacy Champions by Biro KLI** | Forum, Seminar & Workshop | Gedung AA Maramis (General / Kompleks) | 2 hari |
| 2026-07-08 | **Fiscal Heritage Explorer Biro KLI (A2 & C1)** | Heritage Walking Tour & Visit | Gedung A & Gedung C Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mitra kunci dalam amplifikasi narasi publik (earned media) dan kampanye citra Maramis sebagai ruang publik terbuka yang ramah dan inspiratif.

---

### 2.7. Direktorat Jenderal Pengelolaan Pembiayaan dan Risiko (DJPPR)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **3 Kegiatan** | **3 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (2), Loading & Technical Setup (1)

#### A. Profil Singkat & Latar Belakang
Unit Eselon I Kemenkeu pengelola portofolio utang negara, Surat Berharga Negara (SBN), Surat Berharga Syariah Negara (SBSN), pinjaman luar negeri, kerja sama pemerintah dan badan usaha (KPBU), serta mitigasi risiko keuangan negara.

#### B. Karakteristik Audiens & Sasaran
Pimpinan dan analis kebijakan pembiayaan negara, perbankan investasi, dealer utama SBN, dan jajaran internal DJPPR.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menghubungkan warisan sejarah pendanaan negara masa kemerdekaan (Oeang Republik Indonesia) dengan rapat koordinasi strategis dan tur edukasi heritage staf.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-14 | **Walking tour setelah rapat DJPPR** | Heritage Walking Tour & Visit | Gedung C Lantai 2 | 1 hari |
| 2025-10-21 | **LOADING C1 DJPPR** | Loading & Technical Setup | Gedung C Lantai 1 | 1 hari |
| 2025-10-22 | **Walking Tour DJPPR** | Heritage Walking Tour & Visit | Gedung C Lantai 1 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa internal dengan 3 kegiatan (3 hari). Sangat relevan untuk acara peluncuran obligasi ritel bertema warisan bangsa (green sukuk / heritage bond).

---

### 2.8. Direktorat Jenderal Perbendaharaan (DJPb)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **3 Kegiatan** | **3 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1), Heritage Walking Tour & Visit (1), Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Unit Eselon I Kemenkeu pengelola kas negara, perbendaharaan, penyaluran transfer ke daerah, dan pelaporan keuangan pemerintah pusat. Kantor pusatnya berlokasi di kompleks Lapangan Banteng.

#### B. Karakteristik Audiens & Sasaran
Dirjen Perbendaharaan, jajaran auditor Badan Pemeriksa Keuangan (BPK RI), delegasi internasional (Kementerian Keuangan Republik Bangladesh), dan pejabat perbendaharaan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Melakukan entry meeting pemeriksaan BPK yang memerlukan ketenangan dan privasi formal, sesi foto diplomasi bilateral, dan tur apresiasi pimpinan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-09 | **Sesi Foto Dit SITP - DJPb feat. MoF Republik Bangladesh** | Photoshoot & Fashion Show | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-03-04 | **Walking tour Dirjen Perben** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-26 | **Entry Meeting DJPB bersama BPK (Bpk Herawan)** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Pengguna berulang (3 kegiatan, 3 hari) untuk agenda akuntabilitas negara dan kunjungan tamu kehormatan luar negeri.

---

### 2.9. Sekretariat Jenderal Kemenkeu (Setjen Kemenkeu)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **3 Kegiatan** | **3 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Forum, Seminar & Workshop (1), Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Unit pengoordinasi utama manajemen, organisasi, tata laksana, hukum, komunikasi, dan rumah tangga di seluruh lingkungan Kementerian Keuangan.

#### B. Karakteristik Audiens & Sasaran
Pejabat Eselon I & II wanita (Ibu-Ibu Dharma Wanita / Pejabat Kemenkeu), pranata humas se-Kemenkeu, dan staf pendukung manajerial.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memerlukan ruang serbaguna prestisius untuk program pelatihan kehumasan tingkat kementerian serta latar foto monumental arsitektural untuk sesi dokumentasi kepemimpinan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-15 | **Loading (C.2.3 C.2.4 dan C2.13) Peningkatan Kompetensi Kehumasan Sekretariat Jenderal Tahun 2025-PIC Thoriq** | Loading & Technical Setup | Gedung C Lantai 2 (C.2.13, C.2.4, C.2.3) | 1 hari |
| 2025-12-16 | **Peningkatan Kompetensi Kehumasan Sekretariat Jenderal Tahun 2025-PIC Thoriq** | Forum, Seminar & Workshop | Gedung C Lantai 2 (C.2.13, C.2.4, C.2.3) | 1 hari |
| 2026-04-14 | **Sesi Foto Ibu-Ibu Pejabat Eselon 1 & 2 Kemenkeu** | Photoshoot & Fashion Show | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Pengguna reguler (3 kegiatan, 3 hari). Pemangku kepentingan langsung dalam alokasi anggaran operasional dan kebijakan internal pemanfaatan gedung.

---

### 2.10. Direktorat Jenderal Stabilitas dan Pengembangan Sektor Keuangan (DJSPSK Kemenkeu)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **3 Kegiatan** | **5 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1), Loading & Technical Setup (1), Forum, Seminar & Workshop (1)

#### A. Profil Singkat & Latar Belakang
Unit Eselon I termuda Kementerian Keuangan yang dibentuk sebagai amanat UU Nomor 4 Tahun 2023 tentang Pengembangan dan Penguatan Sektor Keuangan (UU P2SK). Berfokus pada perumusan kebijakan stabilitas sistem keuangan dan pengawasan profesi keuangan.

#### B. Karakteristik Audiens & Sasaran
Regulator audit regional se-Asia Tenggara (ASEAN Audit Regulators Group), Dewan Standar Akuntansi, profesi akuntan publik, dan pakar perbankan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan workshop inspeksi audit tingkat regional ASEAN (AARG Inspection Workshop) yang memerlukan ruang konferensi eksklusif dengan fasilitas modern di tengah suasana bersejarah.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-08-04 | **DJSPSK** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-31 | **Loading DJSPSK (Gd. C)** | Loading & Technical Setup | Gedung C | 1 hari |
| 2026-09-01 s.d. 2026-09-03 | **ASEAN Audit Regulators Group Inspection Workshop DJSPSK (all Gd C2)** | Forum, Seminar & Workshop | Gedung C Lantai 2 | 3 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa signifikan (3 pemesanan, 5 hari okupansi). Klien ideal untuk konferensi dan simposium kebijakan finansial multilateral tingkat regional.

---

### 2.11. Lembaga Dana Kerjasama Pembangunan Internasional (LDKPI / Indonesian AID)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Lembaga Non-Eselon Kementerian Keuangan RI
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Forum, Seminar & Workshop (1)

#### A. Profil Singkat & Latar Belakang
Lembaga pengelola dana hibah kerja sama pembangunan luar negeri pemerintah Indonesia (Indonesian Agency for International Development / Indonesian AID) yang menyalurkan bantuan ke negara-negara sahabat di kawasan Pasifik, Asia, dan Afrika.

#### B. Karakteristik Audiens & Sasaran
Delegasi negara anggota Islamic Development Bank (IsDB), perwakilan kementerian luar negeri negara mitra, dan pimpinan lembaga multilateral.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan 'Dialogue Meeting IsDB Member Countries' yang menampilkan kematangan diplomasi pembangunan Indonesia di dalam ruang bernilai sejarah tinggi.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-06 | **Tech Meet sebelum loading LDKPI** | Loading & Technical Setup | Gedung C Lantai 2 | 1 hari |
| 2025-10-07 | **LDKPI - Dialogue Meeting IsDB Member Countries** | Forum, Seminar & Workshop | Gedung C Lantai 2 (C.2.3) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa dengan 2 kegiatan (2 hari). Potensial untuk pertemuan bilateral, workshop diplomatik Selatan-Selatan, dan forum multilateral berkala.

---

### 2.12. Biro Advokasi & Hukum Kemenkeu

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (1), Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Unit kerja di bawah Setjen Kemenkeu yang bertindak sebagai kuasa hukum negara dalam penanganan sengketa hukum perdata, tata usaha negara, uji materi perundang-undangan fiskal di MK, dan perumusan regulasi.

#### B. Karakteristik Audiens & Sasaran
Pimpinan Kemenkeu, tim advokasi hukum fiskal, praktisi hukum tata negara, dan konsultan hukum pemerintah.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Konsinyering rapat pimpinan (Kemenkeu Leaders Offsite Meeting) serta rapat tertutup telaah hukum di Ruang Majapahit & Ruang Kutai yang hening dan terlindungi dari interupsi publik.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-24 | **Kemenkeu Leaders Offsite Meeting - PIC Pushaka Kemenkeu** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-30 | **R. Majapahit & R. Kutai (Biro Advokasi Kemenkeu)** | Corporate & Institutional Event | Gedung Utama (Historical Halls) (Ruang Majapahit, Ruang Kutai) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Pengguna berulang (2 kegiatan, 2 hari) untuk pertemuan strategis tertutup (closed-door executive alignment meetings).

---

### 2.13. Biro Sumber Daya Manusia (SDM Kemenkeu)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **2 Kegiatan** | **3 Hari Okupansi** | **Kategori Acara:** Forum, Seminar & Workshop (2)

#### A. Profil Singkat & Latar Belakang
Pengelola kebijakan manajemen sumber daya manusia aparatur, pengembangan talenta, kesejahteraan pegawai, dan kesetaraan gender di lingkungan Kementerian Keuangan.

#### B. Karakteristik Audiens & Sasaran
Pejabat pengelola SDM, pembicara internasional, aparatur sipil negara wanita, dan perwakilan kementerian/lembaga terkait pemberdayaan perempuan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan seminar dan forum diskusi internasional 'Empowering Women in Civil Service' serta lokakarya pengembangan kapasitas SDM.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-12 s.d. 2025-11-13 | **Seminar & FGD Biro SDM** | Forum, Seminar & Workshop | Gedung C Lantai 2 | 2 hari |
| 2026-08-27 | **International seminar empowering women - biro sdm (up bu vivi)** | Forum, Seminar & Workshop | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Pengguna berulang (2 kegiatan, 2 hari). Target pengguna reguler untuk program corporate university dan executive training program.

---

### 2.14. Direktorat TSI / SITP Kemenkeu

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Kementerian Keuangan RI (Internal)
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Unit pengembang sistem teknologi informasi, infrastruktur digital, integrasi perbendaharaan, dan tata kelola TI di bawah DJPb dan Sekretariat Jenderal.

#### B. Karakteristik Audiens & Sasaran
Pimpinan TI kementerian, arsitek sistem CoreAPBN, dan delegasi teknis kementerian.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memanfaatkan fasad tangga neoklasik dan selasar Gedung C2 untuk sesi foto profil resmi tim pimpinan TI yang menggabungkan modernitas teknologi dengan marwah sejarah gedung.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-13 | **Foto Profil Direktorat TSI** | Photoshoot & Fashion Show | Gedung C Lantai 2 (Selasar / Tangga Masuk) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien internal untuk photoshoot institusional dan pertemuan konsinyering teknologi informasi.

---

### 2.15. Mahkamah Konstitusi RI (MK)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Lembaga Tinggi Negara / Peradilan Konstitusi
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (2)

#### A. Profil Singkat & Latar Belakang
Lembaga tinggi peradilan dalam sistem ketatanegaraan Indonesia yang memegang kekuasaan kehakiman dalam menguji undang-undang terhadap UUD 1945 dan memutus sengketa kewenangan lembaga negara.

#### B. Karakteristik Audiens & Sasaran
Hakim Konstitusi, Panitera, pejabat struktural kepaniteraan, dan peneliti hukum tata negara.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memerlukan lokasi rapat konsinyering di luar gedung kantor utama (offsite meeting) dengan atmosfer berwibawa, privat, dan sarat nilai kenegaraan di pusat kota Jakarta.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-30 | **Rapat Mahkamah Konstitusi** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |
| 2026-07-14 | **Agenda MK** | Official Meeting, Ceremony & Gala | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa eksternal kementerian/lembaga tinggi (2 kegiatan, 2 hari). Membuktikan daya tarik Maramis bagi lembaga yudikatif dan peradilan nasional.

---

### 2.16. Pemerintah Provinsi DKI Jakarta (Pemprov DKI)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Pemerintah Daerah Khusus Ibukota
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Pemerintah daerah provinsi ibu kota yang mengelola kawasan perkotaan, pelestarian cagar budaya, dan ekonomi metropolitan Jakarta.

#### B. Karakteristik Audiens & Sasaran
Gubernur/Pj. Gubernur DKI Jakarta, Forkopimda DKI Jakarta, jajaran kepala dinas, tokoh masyarakat Betawi, dan budayawan ibu kota.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memperingati Hari Ulang Tahun (HUT) DKI Jakarta di salah satu bangunan tertua dan termegah di pusat kota yang menjadi bagian tak terpisahkan dari sejarah tata ruang Weltevreden.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-06-22 | **HUT DKI Jakarta** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mitra pemerintah daerah strategis. Menjadi pintu gerbang integrasi Maramis ke dalam agenda resmi pariwisata dan festival budaya tahunan Pemprov DKI.

---

### 2.17. Dinas Pariwisata dan Ekonomi Kreatif DKI Jakarta (Disparekraf DKI)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Pemerintah Daerah / Organisasi Perangkat Daerah
> **Statistik Sewa:** **4 Kegiatan** | **4 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (2), Corporate & Institutional Event (2)

#### A. Profil Singkat & Latar Belakang
Perangkat daerah yang bertanggung jawab atas pengembangan destinasi wisata, promosi pariwisata urban, kurasi ekonomi kreatif, dan pelestarian seni budaya di DKI Jakarta.

#### B. Karakteristik Audiens & Sasaran
Pelaku usaha pariwisata, asosiasi pemandu wisata, kurator seni rupa, desainer kreatif, dan stakeholder perhotelan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan rapat koordinasi strategis dan aktivasi subsektor ekonomi kreatif di koridor cagar budaya Pasar Baru – Lapangan Banteng.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-17 | **Loading Kegiatan Disparekraf dan PGN** | Loading & Technical Setup | Gedung C Lantai 2 | 1 hari |
| 2025-12-19 | **C2.2 C2.11 C2.12 & C2.13 Disparekraf Prov DKI Jakarta** | Corporate & Institutional Event | Gedung C Lantai 2 (C.2.13, C.2.12, C.2.11, C.2.2) | 1 hari |
| 2026-10-20 | **Loading disparekraf** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-10-21 | **Disparekraf (tbc)** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa eksternal berulang (4 kegiatan, 4 hari). Mitra promosi terpenting untuk memposisikan Maramis sebagai 'anchor destination' pariwisata heritage Jakarta.

---

### 2.18. Dinas Komunikasi, Informatika dan Statistik DKI Jakarta (Diskominfotik DKI)

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Pemerintah Daerah / Organisasi Perangkat Daerah
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Organisasi Perangkat Daerah yang mengampu pengelolaan portal resmi, integrasi satu data pemerintah, layanan komunikasi publik, dan statistik sektoral Jakarta.

#### B. Karakteristik Audiens & Sasaran
Kepala OPD se-DKI, perwakilan Kementerian PPN/Bappenas, akademisi data sains, dan insan pers ibu kota.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memilih Gedung C Lantai 2 sebagai tempat perhelatan akbar 'Peluncuran Satu Data DKI Jakarta' untuk memberikan kesan monumental dan berwibawa pada transformasi data ibu kota.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-11 | **Diskominfotik Jakarta - Peluncuran Satu Data** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien pemerintah untuk peluncuran kebijakan publik dan seremoni program strategis daerah.

---

### 2.19. IKKT Pragati Wira Anggini Cabang BS Otmilti II Jakarta

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Organisasi Istri Prajurit / Instansi Militer-Hukum
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Organisasi kemasyarakatan yang menghimpun istri prajurit TNI dan PNS di lingkungan Pengadilan Militer Tinggi II dan Oditurat Militer Tinggi II Jakarta.

#### B. Karakteristik Audiens & Sasaran
Pengurus dan anggota IKKT Pragati Wira Anggini, pimpinan Otmilti II, dan keluarga besar korps militer hukum.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memanfaatkan arsitektur kolonial neoklasik yang anggun untuk sesi pemotretan resmi seragam organisasi (*official photoshoot*) di selasar Gedung C2.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-09 | **IKKT Otmilti II Jakarta - Photoshoot** | Photoshoot & Fashion Show | Gedung C Lantai 2 (Selasar / Tangga Masuk) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Membuka peluang bagi segmen organisasi kedinasan, Dharma Pertiwi, dan ikatan alumni kedinasan untuk sesi dokumentasi kenegaraan.

---

### 2.20. Ministry of Economy and Finance of Cambodia

> **Kategori Klien:** `Government` | **Sub-Sektor / Industri:** Pemerintah Asing / Kementerian Keuangan Kerajaan Kamboja
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Kementerian pemerintah pusat Kerajaan Kamboja yang membidangi perencanaan ekonomi nasional, anggaran negara, perpajakan, dan pengelolaan aset publik.

#### B. Karakteristik Audiens & Sasaran
Delegasi pimpinan Kementerian Keuangan Kamboja, pejabat diplomatik kedutaan besar, dan pendamping dari Kementerian Keuangan RI.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Melakukan kunjungan studi banding (*study visit & heritage walking tour*) untuk mempelajari tata kelola konservasi dan pemanfaatan komersial aset sejarah kementerian di Indonesia.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-17 | **Study Visit Kemenkeu Kamboja (Tour)** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien benchmarking internasional yang mempertegas reputasi Maramis di mata lembaga keuangan negara sahabat di kawasan regional ASEAN.

---

## 3. Profil Penyewa: Kategori State-Owned Enterprises (BUMN & Lembaga Keuangan Khusus)

Kategori ini mencakup Badan Usaha Milik Negara (BUMN) komersial dan lembaga keuangan dengan mandat khusus (Special Mission Vehicle / SMV) di bawah pembinaan Kementerian Keuangan. Karakteristik sewa berfokus pada rapat kerja pimpinan eksekutif, pertemuan pemangku kepentingan industri strategis, dan temu bisnis perumahan serta ekspor nasional.

### 3.1. PT Bank Negara Indonesia (Persero) Tbk (Bank BNI)

> **Kategori Klien:** `State-Owned Enterprise (BUMN)` | **Sub-Sektor / Industri:** BUMN Perbankan Komersial & Jasa Keuangan
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Bank BUMN tertua yang didirikan pasca kemerdekaan RI (5 Juli 1946) dan pernah bertindak sebagai bank sentral serta penerbit Oeang Republik Indonesia (ORI). Bank komersial papan atas dengan jaringan internasional luas.

#### B. Karakteristik Audiens & Sasaran
Direksi, Senior Executive Vice President (SEVP), General Manager, dan 40 pimpinan divisi strategis BNI.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
BNI memiliki pertalian sejarah yang sangat erat dengan lahirnya uang Republik Indonesia (ORI) di bawah Menteri Keuangan A.A. Maramis. Rapat internal di Ruang VIP Gedung C2 membangkitkan kebanggaan historis identitas BNI.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-16 | **Rapat internal BANK BNI** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 (Ruang VIP (Gd C)) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa BUMN bernilai tinggi. Sangat potensial untuk kerja sama sponsorship jangka panjang, hak penamaan ruang (naming rights / BNI Lounge), dan gala dinner korporat tahunan.

---

### 3.2. PT Perusahaan Gas Negara Tbk (PGN)

> **Kategori Klien:** `State-Owned Enterprise (BUMN)` | **Sub-Sektor / Industri:** BUMN Energi / Subholding Gas Pertamina
> **Statistik Sewa:** **1 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Subholding Gas PT Pertamina (Persero) yang menjadi pengelola infrastruktur dan distribusi gas bumi terbesar di Indonesia dengan jaringan pipa gas ribuan kilometer.

#### B. Karakteristik Audiens & Sasaran
Manajemen senior PGN, kepala divisi komersial & operasional, dan staf manajerial.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Membutuhkan ruang rapat eksklusif, privat, dan prestisius (Ruang C.2.3 / Sriwijaya) untuk rapat koordinasi internal tingkat pimpinan selama 2 hari berturut-turut.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-18 s.d. 2025-12-19 | **internal meeting PGN-PIC Citra** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 (C.2.3) | 2 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa korporat BUMN dengan durasi multi-hari. Potensial untuk paket rapat direksi berkala, town hall pimpinan, dan peluncuran laporan tahunan (annual report launch).

---

### 3.3. PT Sarana Multigriya Finansial (Persero) (SMF)

> **Kategori Klien:** `State-Owned Enterprise (BUMN)` | **Sub-Sektor / Industri:** BUMN / Special Mission Vehicle (SMV) Kementerian Keuangan
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Badan Usaha Milik Negara di bawah pembinaan Kemenkeu yang bertugas membangun dan mengembangkan pasar pembiayaan sekunder perumahan (mortgage secondary market) di Indonesia.

#### B. Karakteristik Audiens & Sasaran
Dewan Direksi SMF, pejabat Bank Indonesia (BI), perbankan penyalur KPR, dan pelaku industri properti nasional.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan forum tingkat tinggi 'Event SMF x Bank Indonesia' di Gedung C2 yang membutuhkan suasana prestisius untuk menyelaraskan kebijakan pembiayaan perumahan nasional.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-20 | **Event SMF X Bank Indonesia** | Corporate & Institutional Event | Gedung C Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Jembatan strategis ke ekosistem BUMN Special Mission Vehicle (SMV) Kemenkeu lainnya (seperti SMI, PII, Geodipa) untuk pemanfaatan Maramis sebagai meeting hub resmi.

---

### 3.4. Lembaga Pembiayaan Ekspor Indonesia (LPEI / Indonesia Eximbank)

> **Kategori Klien:** `State-Owned Enterprise (BUMN)` | **Sub-Sektor / Industri:** Lembaga Keuangan Khusus / SMV Kemenkeu (Sui Generis)
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Lembaga keuangan khusus berstatus lembaga sui generis di bawah Kemenkeu yang bertugas mendukung program ekspor nasional melalui pembiayaan, penjaminan, asuransi, dan jasa konsultasi bagi eksportir.

#### B. Karakteristik Audiens & Sasaran
Pimpinan divisi pembiayaan ekspor, UKM binaan berorientasi ekspor, buyer luar negeri, dan perbankan mitra.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan agenda korporat dan temu bisnis eksportir di gedung berwibawa tinggi yang mencerminkan ketangguhan ekonomi dan kredibilitas ekspor Indonesia.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-09-11 | **LPEI (up. Mas Bayu)** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien korporat sektor keuangan ekspor. Potensial untuk business matching ekspor, showcase produk UKM ekspor binaan, dan investor gathering.

---

## 4. Profil Penyewa: Kategori Private Entity (Korporasi Swasta, Brand Gaya Hidup, & Rumah Produksi)

Kategori ini mencakup perusahaan swasta komersial, jenama fesyen internasional dan nasional, konglomerasi perhiasan mewah, agensi kreatif, serta rumah produksi film layar lebar nasional. Karakteristik utama pemanfaatan adalah pemotretan editorial katalog busana (*fashion photoshoot*), peragaan busana runway catwalk, perayaan ulang tahun korporasi (*anniversary gala*), serta syuting film layar lebar berlatar sejarah kemerdekaan.

### 4.1. Frank & Co. (PT Central Mega Kencana)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Korporasi Swasta / Luxury Diamond & Jewelry
> **Statistik Sewa:** **2 Kegiatan** | **6 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Official Meeting, Ceremony & Gala (1)

#### A. Profil Singkat & Latar Belakang
Merek perhiasan berlian mewah terkemuka di Indonesia di bawah naungan PT Central Mega Kencana (CMK), konglomerasi perhiasan terbesar di Asia Tenggara yang juga menaungi Mondial dan The Palace. Memiliki puluhan gerai di mal-mal papan atas tanah air.

#### B. Karakteristik Audiens & Sasaran
High-Net-Worth Individuals (HNWI), kolektor perhiasan, selebritas, brand ambassador, pimpinan redaksi media mode papan atas, dan klien VVIP.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Merayakan 'Anniversary Frank & Co.' di lokasi yang memancarkan aura kemewahan klasik, keanggunan abadi, dan arsitektur peninggalan bersejarah yang sejalan dengan filosofi 'timeless elegance' produk perhiasan berlian.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-04-21 s.d. 2026-04-22 | **Loading Frank & Co** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 2 hari |
| 2026-04-23 s.d. 2026-04-26 | **Anniversary Frank n Co (Gd. C)** | Official Meeting, Ceremony & Gala | Gedung C Lantai 1 & 2 | 4 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa komersial bernilai sangat tinggi (menyewa seluruh Lantai 1 & 2 Gedung C selama 6 hari penuh, termasuk 2 hari loading). Menjadi studi kasus sukses (benchmark) untuk menarik luxury brands global lainnya (seperti Cartier, Tiffany & Co, Bvlgari).

---

### 4.2. Kinetik (PT Kinetik Unggul Berkarya)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Korporasi Swasta / Sustainability Consultancy & Creative Agency
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Perusahaan konsultansi strategis inovasi, ekonomi sirkular, keberlanjutan (sustainability), dan produksi kreatif yang bermitra dengan perusahaan multinasional dan yayasan filantropi terkemuka.

#### B. Karakteristik Audiens & Sasaran
Eksekutif korporat swasta, pegiat ESG (Environmental, Social, and Governance), mitra start-up ramah lingkungan, dan komunitas kreatif urban.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Mengadakan perhelatan korporat eksklusif selama 2 hari (termasuk 1 hari loading teknis) di gedung bersejarah yang mencerminkan harmoni antara pelestarian warisan masa lalu dan komitmen masa depan berkelanjutan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-08-18 | **Loading acara Kinetik** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-19 | **Acara Kinetik** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien korporat swasta modern. Sangat potensial untuk acara bertema ESG summit, peluncuran laporan keberlanjutan (sustainability report), dan corporate gathering tahunan.

---

### 4.3. PT Aura Vista Global

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Korporasi Swasta / Premium MICE & Corporate Travel Agency
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Perusahaan manajemen perjalanan korporat, MICE (Meetings, Incentives, Conferences, and Exhibitions), dan tur privat eksklusif yang melayani segmen korporasi multinasional dan institusi terkemuka.

#### B. Karakteristik Audiens & Sasaran
Klien korporasi multinasional, delegasi bisnis ekspatriat, dan eksekutif bisnis tingkat tinggi.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan exclusive corporate walking tour & heritage visit sebagai bagian dari paket insentif dan apresiasi mitra bisnis di salah satu cagar budaya terindah di ibu kota.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-27 | **Walking Tour PT Aura Vista Global** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mitra agen perjalanan premium (B2B channel partner) yang dapat secara rutin membawa grup korporasi swasta dan ekspatriat untuk tur privat berbayar.

---

### 4.4. Claude Indonesia (PT Claude Retail Indonesia)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Fashion Kontemporer / Retail Swasta
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Merek fesyen wanita kontemporer terkemuka asal Indonesia dengan desain minimalis-struktural modern yang telah berhasil melakukan ekspansi internasional ke Singapura, Filipina, dan Jepang.

#### B. Karakteristik Audiens & Sasaran
Wanita urban profesional, fashion enthusiasts, influencer gaya hidup modern, dan konsumen muda kelas menengah-atas.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memerlukan lokasi pemotretan editorial katalog busana (editorial photoshoot) di Gedung A Lantai 2 dengan memanfaatkan cahaya alami dari jendela busur lengkung Daendels dan pilar-pilar neoklasik yang dramatis.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-05-22 | **Photoshoot Claude (Gd A)** | Photoshoot & Fashion Show | Gedung A | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien segmen photoshoot mode. Membuka peluang penetapan tarif paket photoshoot komersial terstandardisasi untuk lookbook busana dan kampanye digital.

---

### 4.5. Wearing Klamby (PT Klamby Karya Abadi)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Modest Fashion / Retail Swasta
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Brand modest fashion premium terpopuler di Indonesia yang terkenal dengan kain berilustrasi narasi sejarah dan kekayaan flora/fauna Nusantara. Klamby merupakan merek Indonesia pertama yang menggelar peragaan busana tunggal di ajang London Fashion Week.

#### B. Karakteristik Audiens & Sasaran
Komunitas hijabers urban, wanita muslimah modern kelas menengah ke atas, pecinta busana Nusantara, dan fashion editor.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
DNA jenama Klamby yang berakar pada narasi warisan sejarah Nusantara sangat selaras dengan jiwa dan arsitektur Gedung C Maramis sebagai latar lookbook busana eksklusif.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-06-30 | **Photoshot Klamby (Gd. C)** | Photoshoot & Fashion Show | Gedung C | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien prestisius di industri modest fashion. Berpeluang besar untuk ditingkatkan menjadi peragaan busana runway tahunan atau perayaan hari raya (Hari Raya Collection Show).

---

### 4.6. Love, Bonito (PT Love Bonito Indonesia)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Fashion Multinasional / Retail Internasional
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Merek ritel busana wanita direct-to-consumer (D2C) multinasional terbesar asal Singapura yang beroperasi di berbagai negara Asia Timur dan Tenggara serta didukung pendanaan ventura global.

#### B. Karakteristik Audiens & Sasaran
Wanita karir modern, komunitas penggemar Love Bonito (LB Community), media gaya hidup wanita, dan influencer regional.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan runway megah 'Fashion Show Love, Bonito' di Lantai 1 Gedung C, memanfaatkan lantai marmer selasar dan lorong kolonial beratap tinggi sebagai catwalk megah.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-07-16 | **Fashion show Love Bonito (GD C1)** | Photoshoot & Fashion Show | Gedung C Lantai 1 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa komersial internasional bergengsi. Membuktikan daya tarik Maramis bagi brand ritel multinasional untuk peluncuran koleksi regional (regional collection launch).

---

### 4.7. Love & Flair (PT Gaya Populer Nusantara)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Platform Retail Multi-Brand / Fashion & Lifestyle Swasta
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Platform multi-brand ritel daring dan luring fesyen wanita terkemuka di Indonesia yang mengkurasi puluhan label busana, aksesori, dan sepatu lokal independen berkualitas tinggi.

#### B. Karakteristik Audiens & Sasaran
Gen-Z dan milenial wanita modis, kurator gaya busana, dan konsumen digital savvy.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memilih koridor klasik Lantai 2 Gedung A untuk pemotretan kampanye editorial busana multi-brand berlatar estetika arsitektur vintage kolonial yang sangat disukai di media sosial.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-08-18 | **Photoshoot Love & Flair (Gd. A lantai 2)** | Photoshoot & Fashion Show | Gedung A Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Pelanggan berulang untuk pemotretan kampanye musiman dan potensial menyewa ruang untuk pop-up store curated brands.

---

### 4.8. Day and Knight

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Fashion & Lifestyle Swasta
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Label busana independen kontemporer pria dan wanita yang mengedepankan siluet kasual elegan dan potongan modern.

#### B. Karakteristik Audiens & Sasaran
Kaum muda urban, profesional kreatif, dan penikmat gaya kasual elegan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memanfaatkan pencahayaan dramatis dan tekstur dinding heritage Gedung A Lantai 2 untuk foto katalog koleksi busana terbaru.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-01-21 | **Photoshoot day and knight** | Photoshoot & Fashion Show | Gedung A Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Target segmen reguler untuk sewa ruang pemotretan separuh hari (half-day photoshoot package).

---

### 4.9. Issa Group

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Korporasi Swasta / Holding Gaya Hidup & Komersial
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Grup korporasi swasta yang bergerak di bidang hospitality, gaya hidup, ritel, dan manajemen merek gaya hidup modern.

#### B. Karakteristik Audiens & Sasaran
Pelaku industri gaya hidup, mitra bisnis korporasi, dan konsumen premium.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memanfaatkan ruang eksklusif Ruang Kutai (C.2.13) di Lantai 2 Gedung C untuk pemotretan produk komersial dan visual branding korporat.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-07-30 | **Photoshoot Issa Group (Gd. C2.13)** | Photoshoot & Fashion Show | Gedung C Lantai 2 (C.2.13) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Potensial untuk sewa ruang pertemuan direksi (boardroom rental) dan aktivasi merek gaya hidup.

---

### 4.10. BaTii (Batii Batik)

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Batik Artisan / Luxury Heritage Fashion
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Label busana batik tulis artisan adibusana yang mengkhususkan diri pada kain batik sutra klasik dengan pewarnaan alami dan sentuhan desain modern bernilai tinggi.

#### B. Karakteristik Audiens & Sasaran
Pecinta batik adiluhung, kolektor kain tradisional, sosialita, dan pecinta fesyen warisan budaya.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan perhelatan eksklusif di Ruang Majapahit Gedung Utama yang memadukan keanggunan seni batik tulis keraton dengan kemegahan ruang bersejarah Maramis.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-02-10 | **BaTii (R. Majapahit)** | Corporate & Institutional Event | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Sangat ideal untuk penyelenggaraan trunk show privat, peluncuran karya maestro batik, dan lelang kain wastra Nusantara.

---

### 4.11. Kakena

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Brand Fashion & Aksesori Wanita
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Brand fesyen lokal wanita yang memproduksi busana feminin berkonsep chic, minimalis, dan anggun untuk kebutuhan sehari-hari maupun semi-formal.

#### B. Karakteristik Audiens & Sasaran
Wanita muda urban, profesional muda, dan pengguna media sosial aktif.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Mengambil latar ruang klasik Ruang A.2.3 Gedung A Lantai 2 untuk pemotretan lookbook koleksi fesyen terbaru.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-06-01 | **Photoshoot Kakena (A2.3)** | Photoshoot & Fashion Show | Gedung A Lantai 2 (A.2.3) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien kategori photoshoot berbiaya efisien yang dapat mengisi okupansi ruang pada hari kerja (*weekdays utilization*).

---

### 4.12. Tim Produksi Film Biopik Rose Pandanwangi

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Rumah Produksi / Industri Perfilman Komersial
> **Statistik Sewa:** **3 Kegiatan** | **5 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Film & Media Production (2)

#### A. Profil Singkat & Latar Belakang
Rumah produksi dan tim pembuat film biopik sejarah yang mengangkat kisah hidup maestro seriosa legendaris Indonesia, Rose Pandanwangi, dan suaminya bapak seni lukis modern Indonesia S. Sudjojono.

#### B. Karakteristik Audiens & Sasaran
Kru film profesional, aktor/aktris terkemuka nasional, penata artistik perfilman, dan penonton bioskop Indonesia.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Keaslian arsitektur kolonial neoklasik Daendels dengan pintu tinggi, lantai ubin bersejarah, dan jendela kisi-kisi kayu sangat sempurna sebagai set film era 1940–1960-an tanpa memerlukan banyak modifikasi set buatan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-01-25 | **Loading syuting film rose** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-26 s.d. 2026-01-28 | **Syuting Film Rose** | Film & Media Production | Gedung AA Maramis (General / Kompleks) | 3 hari |
| 2026-01-30 | **Syuting Film Rose Pandanwangi** | Film & Media Production | Gedung A | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa bernilai tinggi (3 kegiatan, total 5 hari okupansi termasuk gladi/loading). Industri perfilman nasional merupakan sumber pendapatan sewa harian tinggi (high daily rate) yang sangat potensial.

---

### 4.13. Tim Produksi Film Epik Sejarah Bung Hatta

> **Kategori Klien:** `Private Entity` | **Sub-Sektor / Industri:** Rumah Produksi / Industri Perfilman Komersial Skala Besar
> **Statistik Sewa:** **1 Kegiatan** | **10 Hari Okupansi** | **Kategori Acara:** Film & Media Production (1)

#### A. Profil Singkat & Latar Belakang
Konsorsium rumah produksi nasional pembuat film layar lebar epik biopik Bung Hatta, mengisahkan perjuangan Proklamator dan Wakil Presiden Pertama RI dalam diplomasi kemerdekaan dan ekonomi kerakyatan.

#### B. Karakteristik Audiens & Sasaran
Ratusan kru produksi sinema, jajaran pemeran film nasional, figuran berpakaian periode 1940-an, dan masyarakat pecinta film sejarah.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Gedung Maramis secara otentik adalah kantor pemerintahan dan kantor Kementerian Keuangan masa revolusi fisik. Keberadaan tangga megah, aula tinggi, dan selasar batu menjadikannya set lokasi paling akurat di Indonesia.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-11-30 s.d. 2026-12-09 | **Produksi film Hatta** | Film & Media Production | Gedung AA Maramis (General / Kompleks) | 10 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa tunggal dengan durasi syuting terpanjang (10 hari berturut-turut pada Nov–Des 2026). Memberikan sumbangan PNBP sewa ruang berskala besar dan nilai promosi luar biasa melalui kredit lokasi film layar lebar.

---

## 5. Profil Penyewa: Kategori Public Entity (Asosiasi, Institusi Pendidikan, Riset, & Festival)

Kategori ini mencakup institusi pendidikan tinggi negeri dan kedinasan, konservatori musik klasik, ikatan alumni universitas, organisasi profesi hukum, asosiasi galeri seni rupa, lembaga riset nirlaba internasional, serta penyelenggara festival industri kreatif berskala besar. Karakteristik sewa memiliki durasi pelaksanaan terpanjang dan mendatangkan puluhan ribu pengunjung.

### 5.1. Gitanada School of Music

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Lembaga Pendidikan Seni & Konservatori Musik
> **Statistik Sewa:** **11 Kegiatan** | **11 Hari Okupansi** | **Kategori Acara:** Concert & Music Performance (8), Loading & Technical Setup (3)

#### A. Profil Singkat & Latar Belakang
Lembaga pendidikan musik klasik terkemuka di Jakarta yang berfokus pada pengajaran piano akustik, biola, vokal klasik, dan resital orkestra anak muda dengan standar kurikulum internasional.

#### B. Karakteristik Audiens & Sasaran
Siswa sekolah musik, musisi muda, orang tua siswa kelas menengah-atas, guru musik klasik, dan pemerhati seni pertunjukan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Ruangan-ruangan di Gedung Maramis (khususnya Ruang Bone C.2.4 dan Aula Gedung C/A) memiliki langit-langit tinggi dan dinding tebal yang menghasilkan resonansi akustik alami sempurna untuk denting piano klasik grand piano.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-23 | **Konser Musik Gitanada School** | Concert & Music Performance | Gedung A Lantai 2 | 1 hari |
| 2026-01-24 | **Loading in & Gladi Resik Konser Gitanada** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-01-25 | **Gitanada School of Music** | Concert & Music Performance | Gedung C Lantai 2 | 1 hari |
| 2026-02-01 | **Gitanada School of music** | Concert & Music Performance | Gedung Utama (Historical Halls) (Ruang Bone) | 1 hari |
| 2026-02-13 | **Loading dan check sound Gitanada** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-02-14 | **Gitanada School of music** | Concert & Music Performance | Gedung Utama (Historical Halls) (Ruang Bone) | 1 hari |
| 2026-05-09 | **Loading piano gitanada** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-05-10 | **Gitanada (R. Bone)** | Concert & Music Performance | Gedung Utama (Historical Halls) (Ruang Bone) | 1 hari |
| 2026-08-02 | **Gitanada** | Concert & Music Performance | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-23 | **Gitanada** | Concert & Music Performance | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-09-27 | **Gitanada (A2)** | Concert & Music Performance | Gedung A Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa berulang paling loyal di sektor seni budaya (11 kali pemesanan konser dan loading teknis piano). Mitra jangka panjang yang ideal untuk program residensi musik akhir pekan ('Maramis Classical Weekend Series').

---

### 5.2. Nelly Music

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Lembaga Musik / Komunitas Seni Musik Akustik
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Concert & Music Performance (1)

#### A. Profil Singkat & Latar Belakang
Lembaga pertunjukan seni musik dan ansambel vokal/akustik independen yang menyelenggarakan resital musik intim dan konser berkala bagi para musisi berbakat.

#### B. Karakteristik Audiens & Sasaran
Penikmat musik kamar (chamber music), keluarga musisi, dan komunitas seni pertunjukan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memilih aula Maramis karena suasana hangat, intim, dan nuansa bangsawan yang mendukung penghayatan musik instrumental akustik.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-10-11 | **Nelly music** | Concert & Music Performance | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Memperkaya portofolio kegiatan akhir pekan berbasis seni pertunjukan dan konser resital musik di Gedung Maramis.

---

### 5.3. Politeknik Keuangan Negara STAN (PKN STAN)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Institusi Pendidikan Tinggi Kedinasan
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (2)

#### A. Profil Singkat & Latar Belakang
Perguruan tinggi kedinasan terdepan di Indonesia di bawah naungan Badan Pendidikan dan Pelatihan Keuangan (BPPK) Kemenkeu yang mencetak aparatur pengelola keuangan dan akuntan negara.

#### B. Karakteristik Audiens & Sasaran
Mahasiswa/mahasiswi tingkat akhir, dosen, pimpinan kampus STAN, dan alumni pengelola keuangan negara.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan kunjungan kampus, tur pengenalan sejarah kantor Kementerian Keuangan (office tour), dan internalisasi nilai integritas bendahara negara di gedung tempat tokoh pendiri bangsa berkantor.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-17 | **Kunjungan PKN STAN** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-20 | **Office tour PKN Stan** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien pendidikan internal (2 kegiatan, 2 hari). Target pemanfaatan rutin untuk orientasi mahasiswa baru dan wisuda kehormatan.

---

### 5.4. Universitas Katolik Parahyangan (Unpar)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Perguruan Tinggi Swasta / Fakultas Teknik Arsitektur
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Salah satu perguruan tinggi swasta tertua dan paling terkemuka di Indonesia, terkenal dengan program studi Arsitektur yang memiliki reputasi tinggi dalam kajian pelestarian cagar budaya dan arsitektur vernakular-kolonial.

#### B. Karakteristik Audiens & Sasaran
Dosen senior arsitektur, peneliti cagar budaya, mahasiswa arsitektur dan magister desain perkotaan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Melakukan studi lapangan langsung (walking tour & architectural study) mengenai metode restorasi adaptif (adaptive reuse) dan teknik konstruksi masonry abad ke-19 pada Gedung Daendels Maramis.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-12-20 | **Walking tour Unpar** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa segmen akademik. Menjadi rujukan laboratorium hidup (living laboratory) bagi riset arsitektur cagar budaya nasional.

---

### 5.5. Ikatan Alumni Universitas (IKA Universitas Padjadjaran & IKA FH Universitas Andalas)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Organisasi Alumni Perguruan Tinggi Terkemuka
> **Statistik Sewa:** **2 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Official Meeting, Ceremony & Gala (1), Forum, Seminar & Workshop (1)

#### A. Profil Singkat & Latar Belakang
Perkumpulan alumni perguruan tinggi negeri terkemuka di Indonesia (Alumni Fakultas Hukum Universitas Andalas dan Ikatan Alumni Universitas Padjadjaran) yang memiliki jejaring luas di jajaran pemerintahan, yudikatif, perbankan, dan advokat.

#### B. Karakteristik Audiens & Sasaran
Tokoh nasional alumni, praktisi hukum terkemuka, anggota DPR, pimpinan BUMN, dan akademisi hukum.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan Reuni Akbar FH Unand serta forum pemikiran hukum dan kebijakan publik bergengsi 'Mochtar Forum 2026' (kerjasama IKA Unpad) di Gedung C2.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-29 | **Reuni FH Univ Andalas** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |
| 2026-10-22 | **Mochtar forum 2026 (up sarah IKA Unpad) C2** | Forum, Seminar & Workshop | Gedung C Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa berulang bergengsi (2 kegiatan, 2 hari). Membuka peluang jejaring ke tokoh-tokoh penting pembuat kebijakan dan asosiasi alumni universitas bergengsi lainnya (seperti ILUNI UI, IA ITB, KAGAMA).

---

### 5.6. PERADI (Perhimpunan Advokat Indonesia)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Organisasi Profesi Advokat Nasional
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Organisasi profesi advokat resmi dan terbesar di Indonesia yang menghimpun puluhan ribu advokat dan penegak hukum di seluruh Indonesia.

#### B. Karakteristik Audiens & Sasaran
Advokat senior, kurator kepailitan, pengurus Dewan Pimpinan Nasional (DPN) PERADI, dan praktisi hukum korporat.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memilih Gedung C Lantai 2 untuk perhelatan rapat koordinasi advokat karena wibawa arsitektur klasik Maramis yang mencerminkan keteguhan dan marwah penegakan hukum.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-05-25 | **Acara Peradi (C2)** | Corporate & Institutional Event | Gedung C Lantai 2 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien organisasi profesi papan atas. Berpotensi untuk penyelenggaraan pendidikan berkelanjutan advokat (CLE), pelantikan advokat baru, dan seminar hukum nasional.

---

### 5.7. Asosiasi Galeri Seni Indonesia (AGSI)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Asosiasi Industri Seni Rupa & Galeri Komersial
> **Statistik Sewa:** **1 Kegiatan** | **30 Hari Okupansi** | **Kategori Acara:** Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Asosiasi resmi yang menaungi galeri-galeri seni rupa komersial terkemuka di Indonesia, bertindak sebagai penggerak ekosistem pasar seni rupa kontemporer dan pelestarian karya maestro nasional.

#### B. Karakteristik Audiens & Sasaran
Kolektor seni rupa papan atas, kurator internasional, seniman terkemuka, pemilik galeri seni, dan pecinta seni budaya.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan pameran akbar seni rupa selama 30 hari penuh di Gedung A Lantai 2, mentransformasi aula heritage Maramis menjadi galeri seni rupa berkelas dunia (world-class contemporary art space).

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-11-01 s.d. 2026-11-30 | **AGSI A2 (tbc)** | Exhibition, Bazaar & Festival | Gedung A Lantai 2 | 30 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa dengan durasi terpanjang dalam sejarah Maramis (30 hari okupansi). Mengukuhkan positioning Gedung Maramis sebagai pusat pameran seni rupa rujukan di kawasan Asia Tenggara.

---

### 5.8. ICRAF Indonesia (World Agroforestry)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Lembaga Riset Internasional / Organisasi Nirlaba Lingkungan
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Pusat penelitian agroforestri internasional yang berafiliasi dengan konsorsium riset CGIAR, berfokus pada mitigasi perubahan iklim, keberlanjutan lanskap pertanian, dan ketahanan pangan di negara-negara berkembang.

#### B. Karakteristik Audiens & Sasaran
Peneliti internasional, diplomat iklim, pejabat kementerian lingkungan hidup & kehutanan, lembaga donor internasional, dan LSM lingkungan.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan simposium kebijakan keberlanjutan di Ruang Majapahit yang hening, bernilai historis, dan mencerminkan komitmen diplomasi lingkungan pemerintah Indonesia.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-05-20 | **ICRAF Indonesia (R. Majapahit)** | Corporate & Institutional Event | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Klien sektor lembaga riset dan donor internasional. Potensial untuk simposium global mengenai pembiayaan hijau (green finance) dan ekonomi sirkular.

---

### 5.9. Semasa di Kota

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Penyelenggara Creative Market & Festival Gaya Hidup Urban
> **Statistik Sewa:** **2 Kegiatan** | **4 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Kurator dan penyelenggara creative pop-up market paling berpengaruh dan terpopuler di Indonesia yang secara konsisten menghidupkan bangunan-bangunan cagar budaya di Jakarta melalui perhelatan pasar kreatif UMKM kriya, kuliner artisanal, fesyen, dan seni.

#### B. Karakteristik Audiens & Sasaran
Puluhan ribu generasi muda, kreator UMKM lokal, turis mancanegara, pecinta desain, dan keluarga muda urban.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Misi Semasa untuk 'menghidupkan kembali kawasan heritage kota' sangat selaras dengan program adaptive reuse Gedung Maramis. Halaman luas dan aula neoklasik Maramis mampu menampung antusiasme pengunjung yang sangat masif.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-12-10 | **Loading Semasa** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-12-11 s.d. 2026-12-13 | **Semasa** | Exhibition, Bazaar & Festival | Gedung AA Maramis (General / Kompleks) | 3 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mitra festival paling berpengaruh dalam menjaring traffic publik massal (4 hari okupansi termasuk loading). Berkontribusi luar biasa pada penciptaan brand awareness Maramis di kalangan generasi muda dan eksposur media sosial.

---

### 5.10. MoveFest Indonesia

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Penyelenggara Festival Gaya Hidup Sehat & Olahraga Urban
> **Statistik Sewa:** **2 Kegiatan** | **4 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Penyelenggara festival gaya hidup urban yang mengintegrasikan aktivitas olahraga santai (wellness, yoga, running), bazar produk gaya hidup aktif, musik akustik, dan temu komunitas pemuda.

#### B. Karakteristik Audiens & Sasaran
Komunitas pelari urban, penggiat kebugaran, generasi muda penikmat musik, dan keluarga urban.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menjadikan seluruh pelataran luar dan aula dalam Gedung AA Maramis sebagai pusat perayaan kebugaran (fitness festival) selama 4 hari (termasuk loading), memadukan gaya hidup modern dengan latar belakang megah gedung bersejarah.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-11-26 | **Loading MoveFest** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-11-27 s.d. 2026-11-29 | **MoveFest 2026** | Exhibition, Bazaar & Festival | Gedung AA Maramis (General / Kompleks) | 3 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa festival skala besar (multi-day booking). Memperluas fungsi Maramis menjadi ruang publik yang inklusif untuk perayaan gaya hidup sehat keluarga dan anak muda.

---

### 5.11. Coffee Conference Indonesia & Jakarta International Coffee Conference (JICC)

> **Kategori Klien:** `Public Entity` | **Sub-Sektor / Industri:** Penyelenggara Konferensi & Expo Industri Kopi
> **Statistik Sewa:** **2 Kegiatan** | **8 Hari Okupansi** | **Kategori Acara:** Loading & Technical Setup (1), Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Entitas penyelenggara platform pameran dagang, simposium ilmiah rantai pasok kopi, kompetisi barista, dan forum temu bisnis petani-eksportir kopi berskala nasional dan internasional (JICC).

#### B. Karakteristik Audiens & Sasaran
Eksportir kopi, diplomat negara produsen/konsumen kopi, barista juara dunia, pemilik kafe specialty, investor agribisnis, dan penikmat kopi.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menghubungkan komoditas kopi Indonesia yang legendaris sejak era kolonial dengan arsitektur kantor peninggalan era Daendels tempat kebijakan ekonomi perdagangan masa lampau berakar.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-01 s.d. 2025-11-05 | **Loading In - Coffee Conference** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 5 hari |
| 2025-11-06 s.d. 2025-11-08 | **Coffee Conference** | Exhibition, Bazaar & Festival | Gedung AA Maramis (General / Kompleks) | 3 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa korporat-festival multi-hari (Coffee Conference: 8 hari; JICC: 8 hari = total 16 hari okupansi). Kategori event industri bernilai ekonomi tinggi yang mendatangkan transaksi bisnis dan sponsorship internasional.

---

## 6. Profil Penyewa: Kategori Community (Komunitas Publik & Penggiat Cagar Budaya)

Kategori ini menghimpun komunitas akar rumput (*grassroots communities*), penggiat jalan kaki perkotaan (*urban walking tours*), pegiat literasi sejarah cagar budaya, serta komunitas gaya hidup sehat dan pemuda. Pemanfaatan utama berfokus pada akhir pekan (*weekend tours*), menjelajahi keindahan arsitektur dan mengedukasi masyarakat luas tentang sejarah gedung.

### 6.1. Eat, Chat, Walk (ECW)

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Wisata Sejarah & Eksplorasi Urban (Heritage Walking Tour)
> **Statistik Sewa:** **10 Kegiatan** | **10 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (10)

#### A. Profil Singkat & Latar Belakang
Komunitas walking tour berbasis sukarelawan terbesar dan paling aktif di Jakarta dengan puluhan ribu pengikut setia di media sosial. Berfokus pada edukasi sejarah arsitektur, kuliner lokal legendaris, dan cerita cagar budaya perkotaan.

#### B. Karakteristik Audiens & Sasaran
Masyarakat urban lintas usia, mahasiswa, keluarga, pecinta fotografi, dan ekspatriat pecinta sejarah lokal.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Gedung A.A. Maramis adalah puncak dari rute tur sejarah Weltevreden. Kesempatan menjelajahi interior gedung bersejarah yang sebelumnya tertutup rapat merupakan daya tarik utama bagi para peserta tur.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-01 | **Walking Tour by Eat, Chat, Walk** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2025-11-22 | **Walking Tour ECW** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2025-12-23 | **Walking Tour by Eat, Chat, Walk** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-02-07 | **Walking Tour by Eat, Chat, Walk** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-05-23 | **Walking tour ECW (pagi)** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-04 | **ECW** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-25 | **ECW** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-09-05 | **ECW walking tour** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-09-12 | **ECW walking tour** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-12-05 | **ECW** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa komunitas paling sering dan berulang (10 sesi walking tour). Menjadi duta komunikasi organik (organic brand ambassador) terdepan dalam menyebarkan citra positif pemanfaatan Maramis kepada masyarakat umum.

---

### 6.2. Wisata Kreatif Jakarta

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Edukasi Cagar Budaya & Wisata Minat Khusus
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Komunitas dan operator tur minat khusus yang diprakarsai oleh pemandu wisata berlisensi dan pegiat literasi sejarah perkotaan Jakarta.

#### B. Karakteristik Audiens & Sasaran
Turis domestik, pelajar, pemerhati tata kota, dan wisatawan pecinta narasi budaya.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Mengangkat narasi sejarah Gedung Putih Daendels dan hubungannya dengan Lapangan Banteng, Monas, dan Kota Tua Jakarta.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-02-14 | **Walking tour wisata kreatif jakarta** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mitra edukasi publik yang konsisten mendatangkan kunjungan wisata minat khusus ke Gedung Maramis.

---

### 6.3. Girls Go Walk

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Gaya Hidup Sehat & Jalan Kaki Wanita Urban
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Komunitas jalan sehat perkotaan khusus wanita yang memadukan aktivitas kebugaran jalan kaki dengan silaturahmi sosial, apresiasi ruang publik kota, dan konten gaya hidup sehat.

#### B. Karakteristik Audiens & Sasaran
Wanita muda urban, mahasiswi, profesional muda perempuan, dan kreator konten digital.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menjadikan kompleks heritage Maramis sebagai titik temu dan rute estetik bagi tur jalan sehat sore hari (15.30 - 17.30).

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-09-19 | **Walking tour girls go walk (15.30 - 17.30)** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Membuktikan bahwa Maramis ramah terhadap komunitas pemuda wanita dan memperkuat citra gedung yang aman, inklusif, dan ramah media sosial (*Instagrammable & accessible*).

---

### 6.4. AKARA Heritage Tour

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Tur Tematik Cagar Budaya
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Komunitas penikmat sejarah yang merancang rute jelajah bangunan tua dengan fokus narasi arsitektur, masa pendudukan, dan biografi tokoh bangsa.

#### B. Karakteristik Audiens & Sasaran
Pecinta sejarah kolonial, arsitek muda, dan fotografer bangunan kuno.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Mengeksplorasi secara detail elemen arsitektur Gedung A Lantai 1 yang kaya akan ornamen klasik abad ke-19.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-10-19 | **AKARA - Heritage Tour** | Heritage Walking Tour & Visit | Gedung A Lantai 1 | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Segmen tur tematik bernilai edukasi tinggi yang mendukung pengenalan mendalam nilai-nilai cagar budaya Maramis.

---

### 6.5. Komunitas Jejak Historia

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Pemerhati Sejarah Nusantara
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Wadah independen pegiat, peneliti muda, dan pecinta sejarah yang aktif mendokumentasikan serta mengadvokasi pelestarian bangunan cagar budaya di Indonesia.

#### B. Karakteristik Audiens & Sasaran
Peneliti sejarah independen, mahasiswa ilmu sejarah, pustakawan, dan penggiat museum.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menelusuri jejak transformasi fungsi Gedung Maramis dari istana gubernur jenderal Daendels, gedung Mahkamah Agung masa Hindia Belanda, hingga kementerian keuangan masa kemerdekaan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-30 | **Walking tour Komunitas Jejak Historia** | Heritage Walking Tour & Visit | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Menjadi mitra diskusi dalam penulisan buku panduan interpretasi sejarah gedung dan penyusunan materi papan informasi (*signage narrative*).

---

### 6.6. Komunitas Sahabat Gizi

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Sosial & Edukasi Kesehatan Masyarakat
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Heritage Walking Tour & Visit (1)

#### A. Profil Singkat & Latar Belakang
Organisasi nirlaba berbasis relawan yang mengampanyekan pemenuhan gizi seimbang, pencegahan stunting, dan gaya hidup sehat berkelanjutan bagi keluarga Indonesia.

#### B. Karakteristik Audiens & Sasaran
Keluarga muda, ibu dan anak, kader kesehatan, dan relawan sosial.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyelenggarakan kegiatan jalan sehat keluarga dan edukasi gizi di seluruh kompleks Gedung AA Maramis yang memiliki area pelataran aman dan bebas polusi kendaraan.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-15 | **Walking Tour - Komunitas Sahabat Gizi** | Heritage Walking Tour & Visit | Seluruh Kompleks Gedung AA Maramis Semua Lantai | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Mendukung citra Gedung Maramis sebagai aset negara yang memberikan dampak sosial positif (*social return on investment*).

---

### 6.7. Komunitas Membaca Raden Saleh

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Komunitas Literasi Seni & Sejarah Budaya
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Corporate & Institutional Event (1)

#### A. Profil Singkat & Latar Belakang
Kelompok pegiat literasi seni rupa yang memfokuskan kajian pada pemikiran, karya lukis, dan korespondensi maestro pelukis beraliran romantisme Raden Saleh Syarif Bustaman.

#### B. Karakteristik Audiens & Sasaran
Penulis seni rupa, kurator independen, sejarawan seni, dan penikmat sastra budaya.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Gedung Maramis dan kawasan Lapangan Banteng memiliki kaitan historis mendalam dengan kehidupan kaum bangsawan dan pergaulan seni budaya masa Raden Saleh tinggal di Batavia.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-08 | **Komunitas Membaca Raden Saleh** | Corporate & Institutional Event | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Memperkaya program aktivasi budaya intelektual (literary salon & book reading) di ruang-ruang rapat bersejarah Maramis.

---

### 6.8. Indy Fest

> **Kategori Klien:** `Community` | **Sub-Sektor / Industri:** Festival Seni & Musik Independen
> **Statistik Sewa:** **1 Kegiatan** | **2 Hari Okupansi** | **Kategori Acara:** Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Platform festival anak muda mandiri yang menggabungkan penampilan band independen, pasar seni zine, ekshibisi karya seni visual alternatif, dan ruang berekspresi generasi muda.

#### B. Karakteristik Audiens & Sasaran
Generasi muda penikmat musik alternatif, seniman muda mandiri, dan mahasiswa kreatif.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Membawa energi pemuda dan musik modern ke dalam lanskap bangunan cagar budaya klasik untuk menciptakan kontras kultural yang memikat.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-11-18 s.d. 2025-11-19 | **Indy Fest** | Exhibition, Bazaar & Festival | Gedung AA Maramis (General / Kompleks) | 2 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Memperluas demografi pengunjung Maramis ke kalangan subkultur anak muda perkotaan yang dinamis.

---

## 7. Profil Penyewa: Kategori Individual (Individu / Desainer & Kurator Mandiri)

Kategori ini mencakup profesional perorangan terkemuka, seperti desainer busana adibusana (*haute couture designer*) dan kurator bazar kriya independen yang secara mandiri mengorganisasi peragaan busana tunggal atau pasar produk lokal berkualitas tinggi.

### 7.1. Stella Lunardy (Fashion Designer)

> **Kategori Klien:** `Individual` | **Sub-Sektor / Industri:** Desainer Busana Adibusana (Haute Couture & Bridal)
> **Statistik Sewa:** **1 Kegiatan** | **1 Hari Okupansi** | **Kategori Acara:** Photoshoot & Fashion Show (1)

#### A. Profil Singkat & Latar Belakang
Desainer busana terkemuka Indonesia lulusan sekolah mode ternama yang mengkhususkan diri pada gaun adibusana (haute couture), gaun pengantin mewah, dan evening gowns bertabur bordir kristal rumit. Karyanya dikenakan oleh selebritas papan atas dan tokoh masyarakat.

#### B. Karakteristik Audiens & Sasaran
Keluarga terkemuka, sosialita, calon pengantin kelas atas, editor majalah mode internasional (Harper's Bazaar, Elle), dan fotografer mode terkemuka.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memilih Gedung AA Maramis sebagai lokasi peragaan busana tunggal (solo runway show) koleksi terbarunya karena kemegahan ruang neoklasik Daendels memberikan atmosfer istana Eropa yang sempurna untuk memamerkan gaun-gaun adibusana impian.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-11-19 | **Fashion show Stella Lunardy** | Photoshoot & Fashion Show | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Membuka pasar persewaan pernikahan mewah (luxury wedding venue) dan peragaan busana desainer solo bernilai tarif sewa premium tinggi. Sangat potensial untuk paket sewa eksklusif satu hari penuh (full-day buyout).

---

### 7.2. Geraldine (Bazar Indonesia by Geraldine)

> **Kategori Klien:** `Individual` | **Sub-Sektor / Industri:** Kurator Bazaar & Wirausaha Kreatif Mandiri
> **Statistik Sewa:** **1 Kegiatan** | **4 Hari Okupansi** | **Kategori Acara:** Exhibition, Bazaar & Festival (1)

#### A. Profil Singkat & Latar Belakang
Kurator dan pengusaha kreatif perorangan yang secara profesional mengorganisasi pameran produk kriya, kain tradisional terkurasi, dan perhiasan artisanal bertajuk 'Bazar Indonesia'.

#### B. Karakteristik Audiens & Sasaran
Pengrajin kriya daerah, pengusaha UMKM batik dan tenun, kolektor perhiasan perak/emas lokal, dan konsumen pecinta produk etnik nusantara.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Menyewa seluruh Lantai 2 Gedung C selama 6 hari penuh (termasuk 2 hari loading) untuk menggelar pameran kriya dan tekstil nusantara di tengah gedung bersejarah yang mencerminkan kekayaan warisan masa lalu.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2026-11-04 s.d. 2026-11-07 | **Bazar indonesia by geraldine (all C2)** | Exhibition, Bazaar & Festival | Gedung C Lantai 2 | 4 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Penyewa komersial skala mingguan yang menghasilkan pendapatan okupansi multi-hari dan menggerakkan transaksi riil produk kriya lokal.

---

## 8. Sesi Operasional & Manajemen Fasilitas Gedung

Bagian ini mencatat alokasi teknis gedung yang dijalankan oleh pengelola internal kompleks untuk memastikan keberlangsungan fisik cagar budaya, sesi pembersihan menyeluruh (*deep cleaning*), jadwal pemeliharaan fasilitas berkala, serta perhelatan terbuka untuk umum (*Open House*).

### 8.1. Manajemen Fasilitas & Operasional Gedung AA Maramis

> **Kategori Klien:** `Operational / Facility Management` | **Sub-Sektor / Industri:** Pengelola Kompleks Aset Cagar Budaya & Logistik Gabungan
> **Statistik Sewa:** **23 Kegiatan** | **25 Hari Okupansi** | **Kategori Acara:** Forum, Seminar & Workshop (1), Heritage Walking Tour & Visit (1), Official Meeting, Ceremony & Gala (2), Loading & Technical Setup (14), Film & Media Production (2), Corporate & Institutional Event (1), Photoshoot & Fashion Show (1), Maintenance & Facility Closure (1)

#### A. Profil Singkat & Latar Belakang
Entitas agregat dalam kalender Teamup yang mencakup manajemen operasional gedung, tim logistik teknis bersama, penghentian sementara fasilitas untuk pemeliharaan rutin (*maintenance closure*), serta perhelatan resmi kenegaraan berskala lintas instansi (seperti Open House Maramis, Jamuan Pimpinan HUT RI, dan Dinner Wamen Kabinet).

#### B. Karakteristik Audiens & Sasaran
Masyarakat umum, tamu kehormatan kenegaraan, kontraktor konservasi, teknisi tata suara & pencahayaan, dan seluruh staf pendukung operasional.

#### C. Motivasi Sewa & Nilai Tambah Gedung A.A. Maramis
Memastikan keteraturan kalender, keselamatan fisik struktur cagar budaya, pemeliharaan sistem mekanikal-elektrikal, serta kelancaran proses loading/unloading seluruh penyewa.

#### D. Riwayat Acara & Pemanfaatan Ruang
| Tanggal | Nama Kegiatan | Kategori Acara | Ruang / Venue | Durasi |
| :--- | :--- | :--- | :--- | :---: |
| 2025-09-29 | **Forum Nasional Sinergi Kerja Sama Ekonomi ASEAN** | Forum, Seminar & Workshop | Gedung C Lantai 2 | 1 hari |
| 2025-09-30 | **Open House Gedung A.A.Maramis** | Heritage Walking Tour & Visit | Seluruh Kompleks Gedung AA Maramis Semua Lantai | 1 hari |
| 2025-10-22 | **Dinner Wakil Menteri Kabinet** | Official Meeting, Ceremony & Gala | Gedung C Lantai 2 | 1 hari |
| 2025-10-23 | **LOADING C2 Kemenkeu LOM** | Loading & Technical Setup | Gedung C Lantai 2 | 1 hari |
| 2026-01-29 | **Loadingout syuting film** | Film & Media Production | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-02-10 | **BaTii (R. Majapahit)** | Corporate & Institutional Event | Gedung Utama (Historical Halls) (Ruang Majapahit) | 1 hari |
| 2026-02-11 | **Loading acara FGD stafsus** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-03-31 | **Loading** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-04-13 | **Loading Barang Ujian Sertifikasi di Gedung A** | Loading & Technical Setup | Gedung A | 1 hari |
| 2026-05-04 | **Loading** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-05-19 | **Loading** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-06-01 | **Photoshoot Kakena (A2.3)** | Photoshoot & Fashion Show | Gedung A Lantai 2 (A.2.3) | 1 hari |
| 2026-06-15 | **Pengambilan footage maramis** | Film & Media Production | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-06-21 | **Loading HUT DKU Jakarta** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-06-24 | **Loading Acara Lelang** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-07-15 | **Loading fashion show** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-06 | **Loading** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-08-17 | **Jamuan pimpinan HUT RI (C1 & C2)** | Official Meeting, Ceremony & Gala | Gedung C Lantai 1 & 2 | 1 hari |
| 2026-09-07 | **Loading Forinves ID** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-09-10 | **Loading** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |
| 2026-10-03 s.d. 2026-10-04 | **Close (maintenance)** | Maintenance & Facility Closure | Gedung AA Maramis (General / Kompleks) | 2 hari |
| 2026-11-02 s.d. 2026-11-03 | **Loading bazar indonesia (all C2)** | Loading & Technical Setup | Gedung C Lantai 2 | 2 hari |
| 2026-11-18 | **Loading fashion show** | Loading & Technical Setup | Gedung AA Maramis (General / Kompleks) | 1 hari |

#### E. Penilaian Persona & Potensi Komersial / Kemitraan
Tolok ukur efisiensi operasional. Menjadi dasar evaluasi standard operating procedure (SOP) loading-in/loading-out, penentuan biaya pembersihan (cleaning service deposit), dan alokasi hari jeda pemeliharaan berkala.

---

## 9. Matriks Pemetaan Pemangku Kepentingan & Rekomendasi Strategis (Strategic Synthesis)

Sebagai kelanjutan analitis yang terintegrasi dengan kerangka **Kajian Strategi Komunikasi** ([skeleton.md](file:///g:/My%20Drive/ANTIGRAVITY/maramis/skeleton.md)), bagian ini memetakan seluruh pihak yang telah memanfaatkan gedung ke dalam kuadran pengaruh-kepentingan (*Power-Interest Matrix*) serta merumuskan persona penyewa dan strategi komersialisasi ke depan.

### 9.1. Matriks Pengaruh dan Kepentingan (*Power-Interest Matrix*)

| Kuadran | Karakteristik Kuadran | Entitas Pemangku Kepentingan | Strategi Komunikasi & Pengelolaan |
| :--- | :--- | :--- | :--- |
| **Kelola Erat (*Manage Closely*)** | **Pengaruh Tinggi, Kepentingan Tinggi** | • DJKN Kemenkeu<br>• Pimpinan Kemenkeu (Menteri/Wamen)<br>• LMAN<br>• Kemenko Perekonomian<br>• OJK | Kemitraan strategis tingkat tinggi, prioritas reservasi kalender kedinasan, pelibatan dalam tata kelola cagar budaya, serta koordinasi protokol VVIP. |
| **Jaga Kepuasan (*Keep Satisfied*)** | **Pengaruh Tinggi, Kepentingan Sedang** | • Pemprov DKI Jakarta & Disparekraf<br>• Mahkamah Konstitusi RI<br>• BUMN Finansial (BNI, SMF, LPEI)<br>• BPK RI | Memastikan kepatuhan regulasi cagar budaya, kelancaran fasilitas ruang rapat berstandar tinggi, dan kemudahan proses administrasi perizinan. |
| **Jaga Keterlibatan (*Keep Informed*)** | **Pengaruh Sedang, Kepentingan Tinggi** | • Komunitas Heritage (ECW, Wisata Kreatif, Girls Go Walk)<br>• Sekolah Seni (Gitanada)<br>• Penyelenggara Festival (Semasa, MoveFest, JICC)<br>• Pelaku Industri Mode & Film (Frank & Co, PH Hatta) | Komunikasi pemasaran berkala, publikasi jadwal ketersediaan ruang, penyediaan materi narasi sejarah terverifikasi, dan program apresiasi tenant loyal. |
| **Pantau Berkala (*Monitor*)** | **Pengaruh Rendah, Kepentingan Sedang** | • Klien photoshoot sporadis<br>• Pengunjung walking tour perorangan<br>• Vendor teknis dan dekorator | Penyediaan kanal informasi digital yang mudah diakses (media sosial resmi, e-booklet tarif, SOP sewa ruang) dan pengawasan kepatuhan konservasi. |

### 9.2. Pemetaan 4 Persona Penyewa Utama (*Tenant Personas*)

1. **The Dignified Statesman (Birokrasi & Lembaga Negara):**
   - *Karakteristik:* Membutuhkan wibawa protokoler, keamanan tinggi, ruang sidang akustik hening, dan katering kenegaraan.
   - *Ruang Favorit:* Ruang Majapahit, Ruang Bone, Ruang Sriwijaya, Gedung C Lantai 2.
   - *Nilai Jual Maramis:* Wibawa sejarah pusat keuangan negara dan lokasi tetangga Lapangan Banteng.
2. **The Aesthetic Creator (Brand Fesyen, Desainer, & Sinema):**
   - *Karakteristik:* Sangat memperhatikan keaslian tekstur visual, pencahayaan alami jendela tinggi, langit-langit lengkung, dan marmer tangga.
   - *Ruang Favorit:* Gedung A Lantai 2, Tangga Utama Gedung C, Selasar Marmer, Koridor Luar.
   - *Nilai Jual Maramis:* Karakter arsitektur Neoklasik Daendels otentik yang tidak dapat ditiru oleh studio modern.
3. **The Cultural & Passionate Community (Komunitas Heritage & Musik Klasik):**
   - *Karakteristik:* Berfokus pada apresiasi cerita sejarah, akustik ruang yang hangat untuk instrumen klasik, serta pengalaman edukatif peserta.
   - *Ruang Favorit:* Ruang Bone (resital piano), seluruh kompleks jalan kaki (outdoor-indoor).
   - *Nilai Jual Maramis:* Nilai historis mendalam dan resonansi akustik ruang berketinggian plafon >5 meter.
4. **The Mass Multiplier (Penyelenggara Festival & Pameran Akbar):**
   - *Karakteristik:* Membutuhkan kapasitas daya tampung ribuan pengunjung, area loading logistik yang luas, daya listrik besar, dan aksesibilitas pusat kota.
   - *Ruang Favorit:* Seluruh Lantai 2 Gedung C, Lantai 2 Gedung A, dan seluruh pelataran halaman Gedung AA Maramis.
   - *Nilai Jual Maramis:* Kapasitas ruang besar di lokasi nol kilometer Jakarta dengan prestige warisan cagar budaya kelas satu.

### 9.3. Rekomendasi Pemasaran & Strategi Monetisasi PNBP

- **Standardisasi Paket Sewa Komersial:** Menetapkan paket bundling resmi, seperti *Fashion Runway Package* (mencakup selasar, ruang ganti VIP, dan sesi loading), *Commercial Photoshoot Half-Day/Full-Day Rate*, dan *Weekend Classical Recital Package*.
- **Insentif 'Musim Sepi' (Bulan Ramadan / Q1):** Mempelajari kekosongan kegiatan pada bulan Maret (hanya 1 kegiatan), pengelola perlu merancang program tematik seperti *Ramadan Heritage Iftar Gathering* dan diskon sewa korporat.
- **Kemitraan Jangka Panjang (*Standing Partnerships*):** Mengunci kontrak tahunan dengan penyewa berulang loyal (seperti Gitanada School of Music, Semasa, dan Eat Chat Walk) dengan skema kalender tahunan terpadu.
- **Sistem Registrasi & Pembayaran Digital:** Mengintegrasikan platform reservasi digital dengan transparansi ketersediaan slot kalender untuk mempercepat proses konfirmasi pemesanan dari rata-rata hitungan minggu menjadi hitungan hari.

---

*Dokumen ini disusun sebagai lampiran analisis pemangku kepentingan dan basis data profil penyewa untuk mendukung penyusunan dokumen Kajian Strategi Komunikasi Gedung A.A. Maramis.*