from domain.entities.entities import Tugas, PengumpulanTugas
from datetime import datetime


def map_tugas(row):
    return Tugas(
        id=row["id"],
        judul=row["judul"],
        deskripsi=row["deskripsi"],
        deadline=datetime.fromisoformat(row["deadline"])
    )


def map_pengumpulan(row):
    return PengumpulanTugas(
        id=row["id"],
        tugas_id=row["tugas_id"],
        nama_mahasiswa=row["nama_mahasiswa"],
        nama_file=row["nama_file"],
        waktu_kumpul=datetime.fromisoformat(row["waktu_kumpul"])
    )
