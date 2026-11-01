# Dokumentasi Test Case

| ID | Jenis | Input | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai `[70, 80, 90]` | Rata-rata `80.0` | Isi setelah menjalankan tes | Belum dijalankan |
| TC02 | Boundary | Nilai `0` | Diterima sebagai nilai valid | Isi setelah menjalankan tes | Belum dijalankan |
| TC03 | Boundary | Nilai `100` | Diterima sebagai nilai valid | Isi setelah menjalankan tes | Belum dijalankan |
| TC04 | Boundary KKM | Nilai `75` dengan KKM `75` | Status Tuntas | Isi setelah menjalankan tes | Belum dijalankan |
| TC05 | Invalid | Nilai `abc` | Ditolak/dilewati sebagai data tidak valid | Isi setelah menjalankan tes | Belum dijalankan |
| TC06 | Invalid | Nilai `101` | Ditolak/dilewati sebagai data tidak valid | Isi setelah menjalankan tes | Belum dijalankan |
| TC07 | Empty | List kosong | Tidak terjadi ZeroDivisionError; rata-rata `0` | Isi setelah menjalankan tes | Belum dijalankan |
| TC08 | File | File tidak ditemukan | FileNotFoundError dengan pesan yang jelas | Isi setelah menjalankan tes | Belum dijalankan |

Jalankan pengujian otomatis dengan `python -m unittest discover -s tests -v`. Setelah tes dijalankan, perbarui kolom Actual result dan Status sesuai hasil yang benar-benar diperoleh.
