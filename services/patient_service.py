from utils.validation import validate_patient_payload

class PatientService:
    def __init__(self, patient_repo):
        self.patient_repo = patient_repo

    def list_patients(self):
        return self.patient_repo.list_all()

    def add_patient(self, data):
        validate_patient_payload(data)
        return self.patient_repo.create(data)

    def get_patient(self, patient_id):
        return self.patient_repo.get(patient_id)

    def update_patient(self, patient_id, data):
        validate_patient_payload(data, partial=True)
        return self.patient_repo.update(patient_id, data)

    def delete_patient(self, patient_id):
        return self.patient_repo.delete(patient_id)