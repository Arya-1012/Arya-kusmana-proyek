# Proyek Rekap dan Analisis Nilai Matematika

## Deskripsi
Program Python berbasis terminal untuk membaca nilai siswa dari CSV, memvalidasi nilai, menghitung statistik, menentukan ketuntasan berdasarkan KKM, dan menyimpan laporan. Proyek ini melanjutkan rancangan Pertemuan 14 dan mengikuti fokus implementasi, pengujian, debugging, dokumentasi, serta Git/GitHub pada Pertemuan 15.

## Fitur
- Membaca data siswa dari `data/contoh_data.csv`.
- Memvalidasi nilai pada rentang 0–100.
- Menghitung jumlah data, rata-rata, nilai minimum, dan maksimum.
- Menentukan status tuntas berdasarkan KKM 75.
- Menangani file yang tidak ditemukan dan format file yang tidak sesuai.
- Menyimpan laporan ke `output/laporan_nilai.txt`.
- Menyertakan pengujian otomatis dengan `unittest`.

## Persyaratan
- Python 3.10 atau versi lebih baru disarankan.
- Tidak memerlukan library eksternal.

## Cara Menjalankan
1. Buka folder proyek di VS Code.
2. Buka terminal melalui **Terminal > New Terminal**.
3. Jalankan perintah:

   ```bash
   python main.py
   ```

4. Lihat ringkasan di terminal dan laporan pada `output/laporan_nilai.txt`.

## Format Data
File CSV harus memiliki header `Nama,Nilai`, misalnya:

```csv
Nama,Nilai
Ayu,85
Budi,78
Citra,92
```

Nilai di luar rentang 0–100, teks nonangka, atau nama kosong akan dilewati dan dicatat sebagai catatan data.

## Struktur Folder
```text
pertemuan-15-implementasi-proyek/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── analisis.py
│   ├── data_io.py
│   └── utilitas.py
├── data/
│   └── contoh_data.csv
├── tests/
│   ├── test_analisis.py
│   └── test_case.md
├── docs/
│   └── bug_log.md
└── output/
    └── .gitkeep
```

## Pengujian
Jalankan dari folder utama proyek:

```bash
python -m unittest discover -s tests -v
```

Pengujian mencakup data normal, list kosong, batas nilai 0 dan 100, input tidak valid, batas KKM, dan statistik.
Catat hasil aktual pada `tests/test_case.md`. Jalankan kembali tes setelah memperbaiki bug sebagai regression check.

## Known Issues
- KKM saat ini ditetapkan 75 di `src/analisis.py`.
- File sumber data ditetapkan pada `data/contoh_data.csv`; ubah sesuai kebutuhan proyek.
- Hasil tes aktual dan riwayat bug harus diperbarui berdasarkan pengujian yang dilakukan tim.

## Anggota dan Kontribusi
Lengkapi bagian ini sesuai kelompok:
- Nama anggota 1: implementasi fungsi utama.
- Nama anggota 2: pengujian dan test case.
- Nama anggota 3: dokumentasi dan GitHub.

## Git dan GitHub
Contoh alur setelah repositori dibuat dan remote dikonfigurasi:

```bash
git status
git add .
git commit -m "feat: implementasi rekap dan analisis nilai"
git push
```

Usahakan satu commit mewakili satu perubahan logis, misalnya `test: menambahkan test case nilai batas` atau `docs: melengkapi README`.

## Referensi dan Bantuan
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14 dan 15, S1 Pendidikan Matematika FKIP Untirta, Tahun Ajaran 2026/2027 Ganjil.
- Dokumentasi Python: https://docs.python.org/3/
- Dokumentasi GitHub: https://docs.github.com/
- Bantuan AI digunakan untuk membantu penyusunan kode dan dokumentasi; tim harus memeriksa, menguji, dan memahami setiap bagian sebelum dikumpulkan.
