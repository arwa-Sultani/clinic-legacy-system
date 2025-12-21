def validate_patient_payload(data, partial=False):
    required = ["name"]
    if not partial:
        for field in required:
            if not data.get(field):
                raise ValueError(f"Missing field: {field}")

def validate_appointment_payload(data, partial=False):
    required = ["patient_id", "date"]
    if not partial:
        for field in required:
            if data.get(field) in (None, ""):
                raise ValueError(f"Missing field: {field}")