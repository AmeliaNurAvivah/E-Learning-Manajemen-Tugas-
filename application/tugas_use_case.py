from datetime import datetime
from task_manage.domain.entities.entities import (PengumpulanTugas ,Tugas )

class PengumpulanTugasUseCase:

    def __init__(self, tugas_repo, pengumpulan_repo):
        self.tugas_repo = tugas_repo
        self.pengumpulan_repo = pengumpulan_repo

    def kumpulkan_tugas(self, tugas_id, mahasiswa_id, file_path):
        tugas = self.tugas_repo.get_by_id(tugas_id)

        if not tugas:
            raise ValueError("Tugas tidak ditemukan")

        if datetime.now() > tugas.deadline:
            raise ValueError("Tenggat waktu telah berakhir")

        pengumpulan = PengumpulanTugas(
            tugas_id=tugas_id,
            mahasiswa_id=mahasiswa_id,
            file_path=file_path
        )

        self.pengumpulan_repo.add(pengumpulan)
        
class TugasUseCase:

    def tambah_tugas(self, judul, deskripsi, matakuliah_id, dosen_id, deadline):
        tugas = Tugas(
            judul=judul,
            deskripsi=deskripsi,
            matakuliah_id=matakuliah_id,
            dosen_id=dosen_id,
            deadline=deadline
        )
        self.tugas_repo.add(tugas)
