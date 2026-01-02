from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import send_from_directory
from application.tugas_use_case import TugasUseCase
from application.pengumpulan_tugas_use_case import PengumpulanTugasUseCase
from infrastructure.services.repositories_impl import (
    TugasRepositoriesImpl,
    PengumpulanTugasRepositoriesImpl
)
from datetime import datetime

tugas_bp = Blueprint("tugas", __name__)

tugas_uc = TugasUseCase(TugasRepositoriesImpl())
pengumpulan_uc = PengumpulanTugasUseCase(
    TugasRepositoriesImpl(),
    PengumpulanTugasRepositoriesImpl()
)


@tugas_bp.route("/")
def dashboard():
    tugas = tugas_uc.lihat_semua_tugas()
    return render_template("pages/dosen/dashboard.html", tugas=tugas, now=datetime.now())


@tugas_bp.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        tugas_uc.tambah_tugas(
            request.form["judul"],
            request.form["deskripsi"],
            datetime.fromisoformat(request.form["deadline"])
        )
        return redirect(url_for("tugas.dashboard"))
    return render_template("pages/tambah_tugas.html")


@tugas_bp.route("/kumpul/<tugas_id>", methods=["POST"])
def kumpul(tugas_id):
    try:
        pengumpulan_uc.kumpulkan_tugas(
            tugas_id,
            request.form["nama"],
            request.files["file"]
        )
        flash("Tugas berhasil dikumpulkan")
    except ValueError as e:
        flash(str(e))
    return redirect(url_for("tugas.dashboard"))

@tugas_bp.route("/uploads/<filename>")
def download_file(filename):
    return send_from_directory("uploads", filename)

@tugas_bp.route("/tugas/<tugas_id>")
def detail_tugas(tugas_id):
    tugas = tugas_uc.detail_tugas(tugas_id)
    pengumpulan = pengumpulan_uc.lihat_pengumpulan(tugas_id)
    return render_template(
        "pages/detail_tugas.html",
        tugas=tugas,
        pengumpulan=pengumpulan
    )

@tugas_bp.route("/dosen")
def dosen_dashboard():
    return render_template(
        "pages/dosen/dashboard.html",
        tugas=tugas_uc.lihat_semua_tugas()
    )


@tugas_bp.route("/dosen/tambah", methods=["GET","POST"])
def dosen_tambah():
    if request.method == "POST":
        tugas_uc.tambah_tugas(
            request.form["judul"],
            request.form["deskripsi"],
            datetime.fromisoformat(request.form["deadline"])
        )
        return redirect("/dosen")
    return render_template("pages/dosen/tambah_tugas.html")


@tugas_bp.route("/dosen/tugas/<tugas_id>")
def dosen_detail(tugas_id):
    return render_template(
        "pages/dosen/detail_tugas.html",
        tugas=tugas_uc.detail_tugas(tugas_id),
        pengumpulan=pengumpulan_uc.lihat_pengumpulan(tugas_id)
    )


@tugas_bp.route("/mahasiswa")
def mahasiswa_dashboard():
    return render_template(
        "pages/mahasiswa/dashboard.html",
        tugas=tugas_uc.lihat_semua_tugas(),
        now=datetime.now()
    )

