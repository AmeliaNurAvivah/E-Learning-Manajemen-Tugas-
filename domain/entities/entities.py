from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tugas:
    id: str
    judul: str
    deskripsi: str
    deadline: datetime


@dataclass
class PengumpulanTugas:
    id: str
    tugas_id: str
    nama_mahasiswa: str
    nama_file: str
    waktu_kumpul: datetime
