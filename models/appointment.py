from dataclasses import dataclass

@dataclass
class Appointment:
    id: int
    patient_id: int
    date: str  # or datetime
    notes: str | None = None