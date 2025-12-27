
from datetime import datetime

class Tugas:
    def __init__(self, id=None, judul=None, deskripsi=None,
                 matakuliah_id=None, dosen_id=None, deadline=None):
        self.id = id
        self.judul = judul
        self.deskripsi = deskripsi
        self.matakuliah_id = matakuliah_id
        self.dosen_id = dosen_id
        self.deadline = deadline  # datetime

class PengumpulanTugas:
    def __init__(self, id=None, tugas_id=None, mahasiswa_id=None,
                 file_path=None, waktu_kumpul=None):
        self.id = id
        self.tugas_id = tugas_id
        self.mahasiswa_id = mahasiswa_id
        self.file_path = file_path
        self.waktu_kumpul = waktu_kumpul or datetime.now()