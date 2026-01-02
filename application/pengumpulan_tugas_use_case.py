import os
from datetime import datetime
from domain.entities.entities import PengumpulanTugas
from domain.repositories.repositories import (
    PengumpulanTugasRepository,
    TugasRepository
)
from .services.id_generator_services import generate_id

UPLOAD_FOLDER = "uploads"


class PengumpulanTugasUseCase:

    def __init__(
        self,
        tugas_repo: TugasRepository,
        pengumpulan_repo: PengumpulanTugasRepository
    ):
        self.tugas_repo = tugas_repo
        self.pengumpulan_repo = pengumpulan_repo

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

    def kumpulkan_tugas(self, tugas_id, nama_mahasiswa, file):
        tugas = self.tugas_repo.get_by_id(tugas_id)

        if not tugas:
            raise ValueError("Tugas tidak ditemukan")

        if datetime.now() > tugas.deadline:
            raise ValueError("Deadline sudah terlewati")

        filename = f"{generate_id()}_{file.filename}"
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        pengumpulan = PengumpulanTugas(
            id=generate_id(),
            tugas_id=tugas_id,
            nama_mahasiswa=nama_mahasiswa,
            nama_file=filename,
            waktu_kumpul=datetime.now()
        )

        self.pengumpulan_repo.add(pengumpulan)

    def lihat_pengumpulan(self, tugas_id):
        return self.pengumpulan_repo.get_by_tugas_id(tugas_id)
