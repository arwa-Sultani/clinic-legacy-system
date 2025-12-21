from utils.validation import validate_appointment_payload

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
        return self.appointment_repo.create(data)

    def get_appointment(self, appointment_id):
        return self.appointment_repo.get(appointment_id)

    def update_appointment(self, appointment_id, data):
        validate_appointment_payload(data, partial=True)
        if "patient_id" in data:
            pid = data.get("patient_id")
            if pid and not self.patient_repo.get(pid):
                raise ValueError("Invalid patient_id")
        return self.appointment_repo.update(appointment_id, data)

    def delete_appointment(self, appointment_id):
        return self.appointment_repo.delete(appointment_id)