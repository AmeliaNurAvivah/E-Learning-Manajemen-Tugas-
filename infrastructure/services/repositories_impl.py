from infrastructure.sqlite_db.db_settings import get_connection
from infrastructure.sqlite_db.mappers import map_tugas, map_pengumpulan
from domain.repositories.repositories import (
    TugasRepository,
    PengumpulanTugasRepository
)


class TugasRepositoriesImpl(TugasRepository):

    def add(self, tugas):
        conn = get_connection()
        conn.execute(
            "INSERT INTO tugas VALUES (?, ?, ?, ?)",
            (tugas.id, tugas.judul, tugas.deskripsi, tugas.deadline.isoformat())
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        rows = conn.execute("SELECT * FROM tugas").fetchall()
        conn.close()
        return [map_tugas(r) for r in rows]

    def get_by_id(self, tugas_id):
        conn = get_connection()
        row = conn.execute(
            "SELECT * FROM tugas WHERE id=?",
            (tugas_id,)
        ).fetchone()
        conn.close()
        return map_tugas(row) if row else None


class PengumpulanTugasRepositoriesImpl(PengumpulanTugasRepository):

    def add(self, pengumpulan):
        conn = get_connection()
        conn.execute(
            "INSERT INTO pengumpulan VALUES (?, ?, ?, ?, ?)",
            (
                pengumpulan.id,
                pengumpulan.tugas_id,
                pengumpulan.nama_mahasiswa,
                pengumpulan.nama_file,
                pengumpulan.waktu_kumpul.isoformat()
            )
        )
        conn.commit()
        conn.close()

    def get_by_tugas_id(self, tugas_id):
        conn = get_connection()
        rows = conn.execute(
            "SELECT * FROM pengumpulan WHERE tugas_id=?",
            (tugas_id,)
        ).fetchall()
        conn.close()
        return [map_pengumpulan(r) for r in rows]
