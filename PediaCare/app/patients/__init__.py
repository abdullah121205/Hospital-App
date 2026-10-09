from datetime import date

from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash
)
from flask_login import login_required
from sqlalchemy import select

from app.extensions import db
from app.models import Patient

patients = Blueprint("patients", __name__)


@patients.route("/add", methods=["GET", "POST"])
@login_required
def add_patient():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        date_of_birth = request.form.get("date_of_birth", "")
        sex = request.form.get("sex", "").strip()
        guardian_name = request.form.get("guardian_name", "").strip()
        guardian_phone = request.form.get("guardian_phone", "").strip()
        address = request.form.get("address", "").strip()

        if not all([
            full_name, date_of_birth, sex,
            guardian_name, guardian_phone
        ]):
            flash("Please fill in all required fields.", "error")
            return render_template("add_patient.html")

        if (
            len(full_name) > 120
            or len(guardian_name) > 120
            or len(guardian_phone) > 20
            or len(address) > 255
        ):
            flash("One or more fields are too long.", "error")
            return render_template("add_patient.html")

        try:
            birth_date = date.fromisoformat(date_of_birth)
        except ValueError:
            flash("Please enter a valid date of birth.", "error")
            return render_template("add_patient.html")

        if birth_date > date.today():
            flash("Date of birth cannot be in the future.", "error")
            return render_template("add_patient.html")

        if sex not in ("Male", "Female", "Other"):
            flash("Please select a valid option.", "error")
            return render_template("add_patient.html")

        patient = Patient(
            full_name=full_name,
            date_of_birth=birth_date,
            sex=sex,
            guardian_name=guardian_name,
            guardian_phone=guardian_phone,
            address=address or None
        )

        try:
            db.session.add(patient)
            db.session.commit()
        except Exception:
            db.session.rollback()
            flash("Unable to save the patient. Please try again.", "error")
            return render_template("add_patient.html")

        flash("Patient registered successfully.", "success")
        return redirect(url_for("patients.list_patients"))

    return render_template("add_patient.html")


@patients.route("/")
@login_required
def list_patients():
    patients_list = db.session.scalars(
        select(Patient).order_by(Patient.id.desc())
    ).all()

    return render_template(
        "patients.html",
        patients=patients_list
    )