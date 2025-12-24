import logging
from utils.validation import validate_patient_payload

logger = logging.getLogger(__name__)

class PatientService:
    def __init__(self, patient_repo):
        self.patient_repo = patient_repo

    def list_patients(self):
        return self.patient_repo.list_all()

    def add_patient(self, data):
        validate_patient_payload(data)
        created = self.patient_repo.create(data)
        logger.info("Patient created id=%s name=%s", created.get("id"), created.get("name"))
        return created

    def get_patient(self, patient_id):
        return self.patient_repo.get(patient_id)

    def update_patient(self, patient_id, data):
        validate_patient_payload(data, partial=True)
        updated = self.patient_repo.update(patient_id, data)
        logger.info("Patient updated id=%s", patient_id)
        return updated

    def delete_patient(self, patient_id):
        deleted = self.patient_repo.delete(patient_id)
        logger.info("Patient deleted id=%s success=%s", patient_id, bool(deleted))
        return deleted