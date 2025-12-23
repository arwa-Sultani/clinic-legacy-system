import re

def _is_valid_phone(phone):
    if phone is None:
        return False
    s = str(phone).strip()
    # Must start with 0 and be exactly 10 digits
    return bool(re.fullmatch(r"0\d{9}", s))

def validate_patient_payload(data, partial=False):
    required = ["name"]
    if not partial:
        for field in required:
            if not data.get(field):
                raise ValueError(f"Missing field: {field}")
    # Validate phone only if provided (to keep API backward-compatible)
    if "phone" in data and data.get("phone") not in (None, ""):
        if not _is_valid_phone(data.get("phone")):
            raise ValueError("not correct phone number: must start with 09")

def validate_appointment_payload(data, partial=False):
    required = ["patient_id", "date"]
    if not partial:
        for field in required:
            if data.get(field) in (None, ""):
                raise ValueError(f"Missing field: {field}")