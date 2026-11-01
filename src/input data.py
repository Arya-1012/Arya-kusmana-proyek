"""Fungsi analisis untuk rekap nilai siswa."""

BATAS_KKM = 75


def hitung_rata_rata(nilai):
    """Mengembalikan rata-rata nilai; 0 jika data kosong."""
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)


def hitung_statistik(nilai):
    """Menghasilkan jumlah, rata-rata, minimum, dan maksimum."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
    }


def hitung_ketuntasan(data_siswa, kkm=BATAS_KKM):
    """Memisahkan siswa tuntas dan belum tuntas berdasarkan KKM."""
    tuntas = [siswa for siswa in data_siswa if siswa["nilai"] >= kkm]
    belum_tuntas = [siswa for siswa in data_siswa if siswa["nilai"] < kkm]
    return tuntas, belum_tuntas
