from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from datetime import date

def appointments_bp(appointment_service):
    bp = Blueprint("appointments", __name__, url_prefix="/appointments")

    @bp.get("/create")
    def create_form():
        # We need patients list for the dropdown; access via service's repo
        # appointment_service has patient_repo reference
        patients = appointment_service.patient_repo.list_all()
        return render_template("appointment_create.html", error=None, patients=patients, today=date.today().isoformat(), form={})

    @bp.post("/create")
    def create_submit():
        form = request.form.to_dict()
        try:
            # coerce patient_id to int if provided
            if "patient_id" in form and form["patient_id"]:
                form["patient_id"] = int(form["patient_id"])
            appointment_service.add_appointment(form)
        except Exception as e:
            patients = appointment_service.patient_repo.list_all()
            return render_template("appointment_create.html", error=str(e), patients=patients, today=date.today().isoformat(), form=form), 400
        return redirect(url_for("appointments.list_appointments"))

    @bp.get("/")
    def list_appointments():
        appts = appointment_service.list_appointments()
        # Enrich with patient object for template compatibility
        if request.accept_mimetypes.accept_html and not request.is_json:
            enriched = []
            for a in appts:
                p = None
                try:
                    pid = a.get("patient_id")
                    if pid is not None:
                        p = appointment_service.patient_repo.get(pid)
                except Exception:
                    p = None
                enriched.append({**a, "patient": p})
            appts = enriched
        if request.accept_mimetypes.accept_html and not request.is_json:
            return render_template("appointments.html", appointments=appts)
        return jsonify(appts)

    @bp.post("/")
    def add_appointment():
        data = request.form.to_dict() if request.form else (request.get_json() or {})
        if "patient_id" in data and isinstance(data["patient_id"], str) and data["patient_id"].isdigit():
            data["patient_id"] = int(data["patient_id"])
        created = appointment_service.add_appointment(data)
        if request.form:
            return redirect(url_for("appointments.list_appointments"))
        return jsonify(created), 201

    return bp