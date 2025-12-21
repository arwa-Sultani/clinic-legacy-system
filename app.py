from flask import Flask, render_template, redirect, url_for
from config import Config
from routes.patients import patients_bp
from routes.appointments import appointments_bp
from repositories.patient_repository import PatientRepository
from repositories.appointment_repository import AppointmentRepository
from services.patient_service import PatientService
from services.appointment_service import AppointmentService

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    # Repositories (in-memory example)
    patient_repo = PatientRepository()
    appointment_repo = AppointmentRepository()

    # Services
    patient_service = PatientService(patient_repo)
    appointment_service = AppointmentService(appointment_repo, patient_repo)

    # Blueprints
    app.register_blueprint(patients_bp(patient_service))
    app.register_blueprint(appointments_bp(appointment_service))

    @app.get("/")
    def index():
        patients = patient_service.list_patients()
        appts = appointment_service.list_appointments()
        # Enrich for dashboard with nested patient
        enriched_appts = []
        for a in appts:
            p = None
            pid = a.get("patient_id")
            if pid is not None:
                p = patient_service.get_patient(pid)
            enriched_appts.append({**a, "patient": p})
        return render_template("index.html", patients=patients, appointments=enriched_appts)

    @app.get("/del_patient/<int:patient_id>")
    def delete_patient_route(patient_id: int):
        patient_service.delete_patient(patient_id)
        return redirect(url_for("patients.list_patients"))

    return app

if __name__ == "__main__":
    create_app().run(debug=True, host="127.0.0.1", port=5050)  # change port if needed