import logging
import os
import time
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, redirect, url_for, request, g, session
from config import Config
from routes.patients import patients_bp
from routes.appointments import appointments_bp
from routes.auth import auth_bp
from repositories.patient_repository import PatientRepository
from repositories.appointment_repository import AppointmentRepository
from services.patient_service import PatientService
from services.appointment_service import AppointmentService

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    # --- Logging setup ---
    logs_dir = os.path.dirname(app.config.get("LOG_FILE", os.path.join(os.getcwd(), "logs", "app.log")))
    os.makedirs(logs_dir, exist_ok=True)

    level_name = str(app.config.get("LOG_LEVEL", "INFO")).upper()
    level = getattr(logging, level_name, logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(app.config.get("LOG_FILE"), maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    app.logger.setLevel(level)
    # Avoid duplicate handlers if create_app is called multiple times in tests
    if not any(isinstance(h, RotatingFileHandler) for h in app.logger.handlers):
        app.logger.addHandler(file_handler)
    if not any(isinstance(h, logging.StreamHandler) for h in app.logger.handlers):
        app.logger.addHandler(stream_handler)

    # Repositories (in-memory example)
    patient_repo = PatientRepository()
    appointment_repo = AppointmentRepository()

    # Services
    patient_service = PatientService(patient_repo)
    appointment_service = AppointmentService(appointment_repo, patient_repo)

    # Blueprints
    app.register_blueprint(patients_bp(patient_service))
    app.register_blueprint(appointments_bp(appointment_service))
    app.register_blueprint(auth_bp())

    # --- Request/Response logging ---
    @app.before_request
    def _log_request():
        g._start_ts = time.time()
        app.logger.info("%s %s from %s", request.method, request.path, request.remote_addr)

    @app.after_request
    def _log_response(resp):
        try:
            dur = (time.time() - getattr(g, "_start_ts", time.time())) * 1000.0
        except Exception:
            dur = -1
        app.logger.info("%s %s -> %s (%.1f ms)", request.method, request.path, resp.status_code, dur)
        return resp

    # Require login for HTML (UI) routes only; keep JSON/API open for tests/integrations
    @app.before_request
    def _require_login_for_html():
        # Allow auth pages, static files, and JSON/API calls
        open_prefixes = ("/auth/", "/static/")
        if request.path == "/auth/login" or request.path.startswith(open_prefixes):
            return None
        # Only guard when browser expects HTML and request isn't JSON
        if request.accept_mimetypes.accept_html and not request.is_json:
            if not session.get("user"):
                next_url = request.full_path if request.query_string else request.path
                return redirect(url_for("auth.login_form", next=next_url))
        return None

    @app.errorhandler(Exception)
    def _handle_exception(e):
        app.logger.exception("Unhandled error during %s %s", request.method, request.path)
        # Let Flask default handler show the error in debug, minimal otherwise
        if app.config.get("DEBUG", False):
            raise e
        return ("Internal Server Error", 500)

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
        app.logger.info("Deleting patient id=%s", patient_id)
        patient_service.delete_patient(patient_id)
        return redirect(url_for("patients.list_patients"))

    return app

if __name__ == "__main__":
    create_app().run(debug=True, host="127.0.0.1", port=5050)  # change port if needed