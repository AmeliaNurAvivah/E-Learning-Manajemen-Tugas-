CREATE TABLE tugas (
    id TEXT PRIMARY KEY,
    judul TEXT NOT NULL,
    deskripsi TEXT,
    deadline TEXT NOT NULL
);

CREATE TABLE pengumpulan (
    id TEXT PRIMARY KEY,
    tugas_id TEXT NOT NULL,
    nama_mahasiswa TEXT NOT NULL,
    nama_file TEXT NOT NULL,
    waktu_kumpul TEXT NOT NULL
);
