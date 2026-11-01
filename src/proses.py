"""Fungsi membaca data siswa dan menyimpan laporan."""
import csv
from pathlib import Path


def validasi_nilai(nilai):
    """Memeriksa nilai numerik dalam rentang 0 sampai 100."""
    try:
        angka = float(nilai)
    except (TypeError, ValueError):
        return None
    if not 0 <= angka <= 100:
        return None
    return angka


def baca_data(lokasi_file):
    """Membaca CSV berkolom Nama,Nilai. Baris tidak valid dilewati."""
    path = Path(lokasi_file)
    if not path.exists():
        raise FileNotFoundError(f"File data tidak ditemukan: {path}")

    data_siswa = []
    masalah = []
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        pembaca = csv.DictReader(file)
        if not pembaca.fieldnames or not {"Nama", "Nilai"}.issubset(pembaca.fieldnames):
            raise ValueError("Format file harus memiliki kolom Nama dan Nilai.")
        for nomor_baris, baris in enumerate(pembaca, start=2):
            nama = (baris.get("Nama") or "").strip()
            nilai = validasi_nilai(baris.get("Nilai"))
            if not nama:
                masalah.append(f"Baris {nomor_baris}: nama kosong, dilewati.")
                continue
            if nilai is None:
                masalah.append(f"Baris {nomor_baris}: nilai tidak valid, dilewati.")
                continue
            data_siswa.append({"nama": nama, "nilai": nilai})
    return data_siswa, masalah


def simpan_laporan(lokasi_file, data_siswa, statistik, tuntas, belum_tuntas, kkm):
    """Menyimpan laporan rekap ke file teks."""
    path = Path(lokasi_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        file.write("LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA\n")
        file.write("=" * 48 + "\n")
        file.write(f"Jumlah data valid : {statistik['jumlah']}\n")
        file.write(f"Rata-rata         : {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai minimum     : {statistik['minimum'] if statistik['minimum'] is not None else '-'}\n")
        file.write(f"Nilai maksimum    : {statistik['maksimum'] if statistik['maksimum'] is not None else '-'}\n")
        file.write(f"KKM               : {kkm}\n\n")
        file.write("DAFTAR SISWA\n")
        for siswa in data_siswa:
            status = "Tuntas" if siswa["nilai"] >= kkm else "Belum tuntas"
            nilai = f"{siswa['nilai']:g}"
            file.write(f"- {siswa['nama']}: {nilai} ({status})\n")
        file.write(f"\nJumlah tuntas     : {len(tuntas)}\n")
        file.write(f"Belum tuntas      : {len(belum_tuntas)}\n")
