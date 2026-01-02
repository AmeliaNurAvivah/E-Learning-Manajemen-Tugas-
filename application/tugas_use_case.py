from datetime import datetime
from domain.entities.entities import Tugas
from domain.repositories.repositories import TugasRepository
from .services.id_generator_services import generate_id


class TugasUseCase:

    def __init__(self, tugas_repo: TugasRepository):
        self.tugas_repo = tugas_repo

    def tambah_tugas(self, judul: str, deskripsi: str, deadline: datetime):
        tugas = Tugas(
            id=generate_id(),
            judul=judul,
            deskripsi=deskripsi,
            deadline=deadline
        )
        self.tugas_repo.add(tugas)

    def lihat_semua_tugas(self) -> list[Tugas]:
        return self.tugas_repo.get_all()

    def detail_tugas(self, tugas_id: str) -> Tugas | None:
        return self.tugas_repo.get_by_id(tugas_id)
