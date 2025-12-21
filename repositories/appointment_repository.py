class AppointmentRepository:
    def __init__(self):
        self._appointments = []
        self._next_id = 1

    def list_all(self):
        return list(self._appointments)

    def get(self, appointment_id):
        return next((a for a in self._appointments if a["id"] == appointment_id), None)

    def create(self, data):
        appt = {"id": self._next_id, **data}
        self._next_id += 1
        self._appointments.append(appt)
        return appt

    def update(self, appointment_id, data):
        appt = self.get(appointment_id)
        if not appt:
            return None
        appt.update(data)
        return appt

    def delete(self, appointment_id):
        before = len(self._appointments)
        self._appointments = [a for a in self._appointments if a["id"] != appointment_id]
        return len(self._appointments) != before