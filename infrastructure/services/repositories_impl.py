from task_manage.domain.repositories.repositories import (TugasRepository, PengumpulanTugasRepository)
from task_manage.infrastructure.sqlite_db.db_settings import get_connection
from task_manage.domain.entities.entities import (Tugas, PengumpulanTugas)
from datetime import datetime

class TugasRepositorySQLite(TugasRepository):

    def add(self, tugas):
        conn = get_connection()
        conn.execute("""
            INSERT INTO tugas (judul, deskripsi, matakuliah_id, dosen_id, deadline)
            VALUES (?, ?, ?, ?, ?)
        """, (
            tugas.judul,
            tugas.deskripsi,
            tugas.matakuliah_id,
            tugas.dosen_id,
            tugas.deadline
        ))
        conn.commit()
        conn.close()

    def get_by_id(self, tugas_id):
        conn = get_connection()
        row = conn.execute("""
            SELECT * FROM tugas WHERE id = ?
        """, (tugas_id,)).fetchone()
        conn.close()

        if not row:
            return None

        return Tugas(
            id=row["id"],
            judul=row["judul"],
            deskripsi=row["deskripsi"],
            matakuliah_id=row["matakuliah_id"],
            dosen_id=row["dosen_id"],
            deadline=datetime.fromisoformat(row["deadline"])
        )

    def get_by_matakuliah(self, matakuliah_id):
        conn = get_connection()
        rows = conn.execute("""
            SELECT * FROM tugas WHERE matakuliah_id = ?
        """, (matakuliah_id,)).fetchall()
        conn.close()

        return [
            Tugas(
                id=r["id"],
                judul=r["judul"],
                deskripsi=r["deskripsi"],
                matakuliah_id=r["matakuliah_id"],
                dosen_id=r["dosen_id"],
                deadline=datetime.fromisoformat(r["deadline"])
            )
            for r in rows
        ]

class PengumpulanTugasRepositorySQLite(PengumpulanTugasRepository):

    def add(self, pengumpulan):
        conn = get_connection()
        conn.execute("""
            INSERT INTO pengumpulan_tugas (tugas_id, mahasiswa_id, file_path, waktu_kumpul)
            VALUES (?, ?, ?, ?)
        """, (
            pengumpulan.tugas_id,
            pengumpulan.mahasiswa_id,
            pengumpulan.file_path,
            pengumpulan.waktu_kumpul
        ))
        conn.commit()
        conn.close()

    def get_by_tugas_and_mahasiswa(self, tugas_id, mahasiswa_id):
        conn = get_connection()
        row = conn.execute("""
            SELECT * FROM pengumpulan_tugas
            WHERE tugas_id = ? AND mahasiswa_id = ?
        """, (tugas_id, mahasiswa_id)).fetchone()
        conn.close()

        if not row:
            return None

        return PengumpulanTugas(
            id=row["id"],
            tugas_id=row["tugas_id"],
            mahasiswa_id=row["mahasiswa_id"],
            file_path=row["file_path"],
            waktu_kumpul=datetime.fromisoformat(row["waktu_kumpul"])
        )

    def get_by_tugas(self, tugas_id):
        conn = get_connection()
        rows = conn.execute("""
            SELECT * FROM pengumpulan_tugas WHERE tugas_id = ?
        """, (tugas_id,)).fetchall()
        conn.close()

        return [
            PengumpulanTugas(
                id=r["id"],
                tugas_id=r["tugas_id"],
                mahasiswa_id=r["mahasiswa_id"],
                file_path=r["file_path"],
                waktu_kumpul=datetime.fromisoformat(r["waktu_kumpul"])
            )
            for r in rows
        ]