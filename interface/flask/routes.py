from flask import Blueprint, render_template, request,session, redirect, url_for, flash
from task_manage.application.tugas_use_case import TugasUseCase
from task_manage.infrastructure.services.repositories_impl import (TugasRepositorySQLite ,
                                                                   PengumpulanTugasRepositorySQLite)
from datetime import datetime
import os

tugas_bp = Blueprint("tugas", __name__, url_prefix="/tugas")

tugas_uc = TugasUseCase


UPLOAD_FOLDER = "flask_app/static/uploads"

@tugas_bp.route("/")
def dashboard_tugas():
    """
    Dashboard utama manajemen tugas
    Ditampilkan saat pertama kali masuk ke modul tugas
    """

    role = session.get("role")  # 'dosen' / 'mahasiswa'

    if role == "dosen":
        tugas_list = tugas_uc.list_tugas_dosen(session.get("user_id"))
    elif role == "mahasiswa":
        tugas_list = tugas_uc.list_tugas_mahasiswa(session.get("user_id"))
    else:
        tugas_list = []

    return render_template(
        "pages/dashboard.html",
        tugas_list=tugas_list,
        role=role
    )


@tugas_bp.route("/dosen/tugas/tambah", methods=["GET", "POST"])
def tambah_tugas():
    if request.method == "POST":
        tugas_uc.tambah_tugas(
            judul=request.form["judul"],
            deskripsi=request.form["deskripsi"],
            matakuliah_id=request.form["matakuliah_id"],
            dosen_id=request.form["dosen_id"],
            deadline=datetime.fromisoformat(request.form["deadline"])
        )
        return redirect(url_for("tugas.daftar_tugas_dosen"))

    return render_template("dosen/tambah_tugas.html")

@tugas_bp.route("/mahasiswa/tugas/<int:tugas_id>/kumpul", methods=["POST"])
def kumpul_tugas(tugas_id):
    file = request.files["file"]
    mahasiswa_id = request.form["mahasiswa_id"]

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        tugas_uc.kumpulkan_tugas(
            tugas_id=tugas_id,
            mahasiswa_id=mahasiswa_id,
            file_path=filepath
        )
    except ValueError as e:
        flash(str(e))
        return redirect(request.referrer)

    return redirect(url_for("tugas.daftar_tugas_mahasiswa"))
