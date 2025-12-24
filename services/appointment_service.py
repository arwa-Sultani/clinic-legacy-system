import logging
from utils.validation import validate_appointment_payload

logger = logging.getLogger(__name__)

class AppointmentService:
    def __init__(self, appointment_repo, patient_repo):
        self.appointment_repo = appointment_repo
        self.patient_repo = patient_repo

    def list_appointments(self):
        return self.appointment_repo.list_all()

    def add_appointment(self, data):
        validate_appointment_payload(data)
        # ensure patient exists
        pid = data.get("patient_id")
        if pid and not self.patient_repo.get(pid):
            raise ValueError("Invalid patient_id")
        created = self.appointment_repo.create(data)
        logger.info("Appointment created id=%s patient_id=%s date=%s", created.get("id"), created.get("patient_id"), created.get("date"))
        return created

    def get_appointment(self, appointment_id):
        return self.appointment_repo.get(appointment_id)

    def update_appointment(self, appointment_id, data):
        validate_appointment_payload(data, partial=True)
        if "patient_id" in data:
            pid = data.get("patient_id")
            if pid and not self.patient_repo.get(pid):
                raise ValueError("Invalid patient_id")
        updated = self.appointment_repo.update(appointment_id, data)
        logger.info("Appointment updated id=%s", appointment_id)
        return updated

    def delete_appointment(self, appointment_id):
        deleted = self.appointment_repo.delete(appointment_id)
        logger.info("Appointment deleted id=%s success=%s", appointment_id, bool(deleted))
        return deleted