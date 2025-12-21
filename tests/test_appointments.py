def test_create_and_list_appointments(client):
    # create patient first
    p = client.post("/patients/", json={"name": "Bob"}).get_json()
    resp = client.post("/appointments/", json={"patient_id": p["id"], "date": "2025-01-01"})
    assert resp.status_code == 201
    appt = resp.get_json()
    assert appt["patient_id"] == p["id"]

    resp = client.get("/appointments/")
    assert resp.status_code == 200
    appts = resp.get_json()
    assert any(a["patient_id"] == p["id"] for a in appts)