from abc import ABC, abstractmethod

class TugasRepository(ABC):

    @abstractmethod
    def add(self, tugas): pass

    @abstractmethod
    def get_by_id(self, tugas_id): pass

    @abstractmethod
    def get_by_matakuliah(self, matakuliah_id): pass

class PengumpulanTugasRepository(ABC):

    @abstractmethod
    def add(self, pengumpulan): pass

    @abstractmethod
    def get_by_tugas_and_mahasiswa(self, tugas_id, mahasiswa_id): pass

    @abstractmethod
    def get_by_tugas(self, tugas_id): pass