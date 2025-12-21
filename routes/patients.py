from flask import Blueprint, request, jsonify, render_template, redirect, url_for

def patients_bp(patient_service):
    bp = Blueprint("patients", __name__, url_prefix="/patients")

    @bp.get("/add")
    def add_patient_form():
        return render_template("patient_add.html", error=None, form={})

    @bp.post("/add")
    def add_patient_submit():
        form = request.form.to_dict()
        try:
            patient_service.add_patient(form)
        except Exception as e:
            return render_template("patient_add.html", error=str(e), form=form), 400
        return redirect(url_for("patients.list_patients"))

    @bp.get("/")
    def list_patients():
        patients = patient_service.list_patients()
        # Render HTML if browser; JSON fallback otherwise
        if request.accept_mimetypes.accept_html and not request.is_json:
            return render_template("patients.html", patients=patients)
        return jsonify(patients)

    @bp.post("/")
    def add_patient():
        data = request.form.to_dict() if request.form else (request.get_json() or {})
        created = patient_service.add_patient(data)
        if request.form:
            return redirect(url_for("patients.list_patients"))
        return jsonify(created), 201

    @bp.get("/<int:patient_id>/edit")
    def edit_patient_form(patient_id: int):
        patient = patient_service.get_patient(patient_id)
        if not patient:
            return ("Not Found", 404)
        return render_template("patient_edit.html", error=None, patient=patient)

    @bp.post("/<int:patient_id>/edit")
    def edit_patient_submit(patient_id: int):
        data = request.form.to_dict()
        try:
            updated = patient_service.update_patient(patient_id, data)
        except Exception as e:
            patient = patient_service.get_patient(patient_id)
            return render_template("patient_edit.html", error=str(e), patient=patient), 400
        if not updated:
            return ("Not Found", 404)
        return redirect(url_for("patients.list_patients"))

    return bp