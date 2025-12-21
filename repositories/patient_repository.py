class PatientRepository:
    def __init__(self):
        self._patients = []
        self._next_id = 1

    def list_all(self):
        return list(self._patients)

    def get(self, patient_id):
        return next((p for p in self._patients if p["id"] == patient_id), None)

    def create(self, data):
        patient = {"id": self._next_id, **data}
        self._next_id += 1
        self._patients.append(patient)
        return patient

    def update(self, patient_id, data):
        patient = self.get(patient_id)
        if not patient:
            return None
        patient.update(data)
        return patient

    def delete(self, patient_id):
        before = len(self._patients)
        self._patients = [p for p in self._patients if p["id"] != patient_id]
        return len(self._patients) != before