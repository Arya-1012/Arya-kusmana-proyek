"""Program utama rekap dan analisis nilai matematika."""
from pathlib import Path
from src.analisis import BATAS_KKM, hitung_statistik, hitung_ketuntasan
from src.data_io import baca_data, simpan_laporan
from src.utilitas import format_nilai

ROOT = Path(__file__).resolve().parent
FILE_DATA = ROOT / "data" / "contoh_data.csv"
FILE_LAPORAN = ROOT / "output" / "laporan_nilai.txt"


def main():
    print("=== REKAP DAN ANALISIS NILAI MATEMATIKA ===")
    try:
        data_siswa, masalah = baca_data(FILE_DATA)
    except (FileNotFoundError, ValueError) as error:
        print(f"Kesalahan membaca data: {error}")
        return

    if not data_siswa:
        print("Tidak ada data valid untuk dianalisis.")
        for pesan in masalah:
            print(f"- {pesan}")
        return

    nilai = [siswa["nilai"] for siswa in data_siswa]
    statistik = hitung_statistik(nilai)
    tuntas, belum_tuntas = hitung_ketuntasan(data_siswa, BATAS_KKM)

    print(f"Jumlah siswa valid : {statistik['jumlah']}")
    print(f"Rata-rata nilai    : {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum      : {format_nilai(statistik['minimum'])}")
    print(f"Nilai maksimum     : {format_nilai(statistik['maksimum'])}")
    print(f"KKM                : {BATAS_KKM}")
    print(f"Tuntas             : {len(tuntas)} siswa")
    print(f"Belum tuntas       : {len(belum_tuntas)} siswa")

    if masalah:
        print("\nCatatan data:")
        for pesan in masalah:
            print(f"- {pesan}")

    simpan_laporan(FILE_LAPORAN, data_siswa, statistik, tuntas, belum_tuntas, BATAS_KKM)
    print(f"\nLaporan disimpan di: {FILE_LAPORAN.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
