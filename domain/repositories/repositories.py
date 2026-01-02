from abc import ABC, abstractmethod
from domain.entities.entities import Tugas, PengumpulanTugas


class TugasRepository(ABC):

    @abstractmethod
    def add(self, tugas: Tugas): pass

    @abstractmethod
    def get_all(self) -> list[Tugas]: pass

    @abstractmethod
    def get_by_id(self, tugas_id: str) -> Tugas | None: pass


class PengumpulanTugasRepository(ABC):

    @abstractmethod
    def add(self, pengumpulan: PengumpulanTugas): pass

    @abstractmethod
    def get_by_tugas_id(self, tugas_id: str) -> list[PengumpulanTugas]: pass
