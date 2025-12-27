CREATE TABLE tugas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT,
    deskripsi TEXT,
    matakuliah_id INTEGER,
    dosen_id INTEGER,
    deadline DATETIME
);

CREATE TABLE pengumpulan_tugas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tugas_id INTEGER,
    mahasiswa_id INTEGER,
    file_path TEXT,
    waktu_kumpul DATETIME
);
