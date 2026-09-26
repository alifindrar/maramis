# Lampiran Data — Analisis Pemanfaatan Gedung A.A. Maramis (Sep 2025 – Des 2026)

> **Sumber:** `1 - ingested/events.csv` (ekspor Teamup Calendar, 172 entri) dan `1 - ingested/daftar_ruangan.csv` (49 unit ruang, Booklet Sept 2026).
> **Tanggal cut-off:** 26 September 2026. Entri setelah tanggal ini diperlakukan sebagai *pipeline* (terjadwal, belum terlaksana).
> **Skrip:** [`analyze.py`](analyze.py); keluaran mentah tersimpan di `_analysis_output.json`.

## 1. Definisi & Catatan Metodologi
- **Kegiatan inti** = entri kalender selain sesi *loading/technical setup* (`is_loading_setup = 0`).
- **Hari terisi unik** = gabungan (union) seluruh tanggal kegiatan + loading, sehingga kegiatan paralel pada hari yang sama tidak dihitung dua kali.
- **Kelompok penyelenggara makro** menggabungkan 17 sektor asal Teamup menjadi 5 kelompok: Kemenkeu (internal); K/L, BUMN & lembaga; Komunitas, pendidikan & seni; Komersial & kreatif; Lainnya/tidak teridentifikasi.
- **Keterbatasan data:** 62,4% kegiatan inti tidak mencantumkan lantai atau ruang. Kalender juga tidak memuat nilai transaksi, jumlah peserta, atau status pembayaran (sewa vs penggunaan internal non-PNBP), sehingga analisis pendapatan tidak dapat dilakukan secara presisi.

## 2. Indikator Utama

| Indikator | Nilai |
| :--- | ---: |
| Total entri kalender | 172 |
| Kegiatan inti / sesi loading | 133 / 39 |
| Total hari-kegiatan (termasuk loading) | 254 |
| Hari loading (overhead teknis) | 45 hari (17,7% dari hari-kegiatan) |
| Hari kalender unik terisi (seluruh periode) | 204 |
| **Hari unik terisi, 12 bulan terakhir (26 Sep 2025 – 26 Sep 2026)** | **153 dari 366 hari = 41,8%** |
| Penyelenggara unik | 58 |
| Penyelenggara teridentifikasi berulang (≥2 kegiatan) | 19 dari 57 → menyumbang 69,4% kegiatan |
| Porsi kegiatan inti pada akhir pekan | 24,1% |
| Kegiatan terlaksana / pipeline | 153 / 19 |

## 3. Tren Bulanan
![Kegiatan bulanan](images/01_kegiatan_bulanan.png)

| Bulan | Entri | Hari | Kegiatan inti |
| :--- | ---: | ---: | ---: |
| Sep-25 | 2 | 2 | 2 |
| Okt-25 | 20 | 21 | 15 |
| Nov-25 | 20 | 28 | 19 |
| Des-25 | 16 | 17 | 13 |
| Jan-26 | 17 | 19 | 13 |
| Feb-26 | 11 | 11 | 8 |
| **Mar-26** | **2** | **2** | **1** |
| Apr-26 | 11 | 17 | 7 |
| Mei-26 | 10 | 12 | 7 |
| Jun-26 | 7 | 9 | 5 |
| Jul-26 | 16 | 20 | 13 |
| Agu-26 | 13 | 13 | 10 |
| Sep-26 | 9 | 11 | 7 |
| Okt-26 (pipeline) | 6 | 7 | 5 |
| Nov-26 (pipeline) | 9 | 60 | 6 |
| Des-26 (pipeline) | 3 | 5 | 2 |

**Temuan:**
1. Puncak terjadi pada Okt–Nov 2025, tepat setelah *Open House* (30 Sep 2025). Hal ini mengindikasikan bahwa momen publikasi mendorong permintaan.
2. Maret 2026 hampir kosong (1 kegiatan). Kemungkinan besar ini efek Ramadan/Idulfitri; periode tersebut perlu program "musim sepi" yang dirancang khusus, misalnya *Ramadan heritage night* atau buka puasa korporat.
3. Pipeline Q4-2026 hanya 18 entri, dibandingkan 56 entri pada Q4-2025. Selisih ini mencerminkan **cakrawala pemesanan yang pendek** (klien memesan dalam hitungan minggu), bukan penurunan permintaan. Implikasinya, komunikasi penjualan harus berjalan terus-menerus, bukan musiman.
4. Nov-26 memuat 60 hari-kegiatan karena pameran AGSI (30 hari), JICC (8 hari), dan Bazar Indonesia. Ini menandai pergeseran ke **kegiatan budaya-komersial berdurasi panjang** yang bernilai tinggi untuk *earned media*.

## 4. Siapa Penggunanya
![Sektor penyelenggara](images/02_sektor_penyelenggara.png)

| Kelompok | Kegiatan inti | Hari |
| :--- | ---: | ---: |
| Kemenkeu (internal) | 45 (34%) | 59 |
| K/L, BUMN & lembaga | 30 (23%) | 31 |
| Komunitas, pendidikan & seni | 29 (22%) | 58 |
| Komersial & kreatif | 20 (15%) | 51 |
| Lainnya/tidak teridentifikasi | 9 (7%) | 10 |

**Temuan:** 57% kegiatan berasal dari lingkungan pemerintah, sehingga citra gedung saat ini adalah "ruang rapat kementerian yang megah". Segmen komersial & kreatif baru 15% dari jumlah kegiatan, tetapi menyumbang 51 hari karena durasinya lebih panjang (festival, film). Penyelenggara berulang teratas: DJKN (13), Kemenko Perekonomian (11), Eat Chat Walk (10), Gitanada School of Music (8), LMAN (7), Pimpinan Kemenkeu (7), OJK (5).

## 5. Jenis Kegiatan
![Kategori](images/03_kategori_kegiatan.png)

| Kategori | Kegiatan | Hari |
| :--- | ---: | ---: |
| Rapat resmi, seremoni & gala | 32 | 36 |
| Heritage walking tour & kunjungan | 25 | 25 |
| Acara korporat & institusional | 22 | 22 |
| Forum, seminar & workshop | 18 | 30 |
| Photoshoot & fashion show | 13 | 13 |
| Konser & pertunjukan musik | 9 | 9 |
| Pameran, bazar & festival | 8 | 56 |
| Produksi film & media | 5 | 16 |
| Pemeliharaan/penutupan | 1 | 2 |

## 6. Pola Hari
![Hari](images/04_hari_kegiatan.png)

Selasa adalah hari tersibuk (27 kegiatan). Akhir pekan hanya 24% kegiatan inti. Namun **64% walking tour berlangsung di akhir pekan**, sehingga segmen publik/komunitas menjadi pengisi alami slot akhir pekan yang kosong dari agenda kedinasan.

## 7. Walking Tour & Akses Publik
![Walking tour](images/05_walking_tour.png)

Tercatat 25 kunjungan/walking tour. Eat Chat Walk (ECW) menyumbang 10 (40%), dengan ritme sekitar bulanan. Operator lain (AKARA, Jejak Historia, Wisata Kreatif Jakarta, Girls Go Walk) masing-masing baru sekali. Akses publik bergantung pada satu mitra. Belum ada program tur reguler milik pengelola sendiri.

## 8. Inventaris vs Pemanfaatan Ruang
![Kapasitas vs pemakaian](images/06_kapasitas_vs_pemakaian.png)

| Lantai | Unit | Kapasitas | Jumlah tarif harian | Kegiatan inti tercatat* |
| :--- | ---: | ---: | ---: | ---: |
| Gd C Lt 1 (paket) | 15 | 950 | Rp125.000.000 (paket) | 4 |
| Gd A Lt 2 | 8 | 350 | Rp37.962.000 | 12 |
| Gd C Lt 2 (ruang Kerajaan Nusantara) | 9 | 990 | Rp95.460.000 | 44 |
| Gd A Lt 3 | 8 | 380 | Rp39.960.000 | 1 |
| Gd C Lt 3 (termasuk aula C3.8, 340 org) | 9 | 1.240 | Rp111.666.000 | **0** |

\*Hanya kegiatan yang mencantumkan lantai; kegiatan lintas lantai dihitung di tiap lantai.

**Temuan:**
- Lantai 2 Gedung C, yang memiliki ruang bernama (Majapahit, Sriwijaya, Bone, Kutai, Ternate, Mataram), adalah produk terlaris. **Ruang yang punya nama lebih mudah dijual dan diingat.** Majapahit disebut 7 kali, Bone 3 kali.
- **Lantai 3 (A & C), 17 unit dengan kapasitas 1.620 orang, praktis belum terjual.** Ini celah komunikasi produk terbesar: aula C3.8 (496 m², 340 orang) adalah ruang terbesar di gedung, tetapi tidak memiliki nama maupun citra.
- 43 dari 49 unit hanya memiliki kode alfanumerik. Kalender Teamup memakai label campuran ("Gedung Utama (Historical Halls)", "R. Majapahit", "C.2.12", "Ruang VIP (Gd C)"). Diperlukan **nomenklatur ruang tunggal** untuk pemasaran dan operasional.
- Rentang tarif per ruang Rp3,44–30,30 juta/hari; median Rp6,16 juta; median tarif per kapasitas sekitar Rp100 ribu/orang/hari.

## 9. Kegiatan Bernilai Media (sinyal *earned media*)
- Kunjungan HM Queen Máxima dari Belanda (OJK, 27 Nov 2025)
- Syuting film *Rose Pandanwangi* (Jan 2026) dan produksi film *Bung Hatta* (30 Nov – 9 Des 2026)
- Coffee Conference (Nov 2025) → Jakarta International Coffee Conference (8–15 Nov 2026)
- Pameran & Lelang Lukisan DJKN (Jun 2026), Pameran AGSI (Nov 2026, tbc), Semasa di Kota (Des 2026), MoveFest (Nov 2026)
- Fashion show Love, Bonito (Jul 2026) dan Stella Lunardy (Nov 2026); photoshoot Klamby, Love & Flair, Claude Indonesia
- Seremoni kenegaraan: Hari Oeang (30 Okt), Jamuan Pimpinan HUT RI (17 Agu), HUT DKI Jakarta (22 Jun)
- *Fiscal Heritage Explorer* Biro KLI (8 Jul 2026), sebuah format edukasi internal yang dapat dikembangkan untuk publik
- Penandatanganan MoU LMAN–MRT Jakarta (17 Des 2025)
