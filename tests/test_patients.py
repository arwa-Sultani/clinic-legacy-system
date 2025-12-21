def test_create_and_list_patients(client):
    resp = client.post("/patients/", json={"name": "Alice"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "Alice"

    resp = client.get("/patients/")
    assert resp.status_code == 200
    patients = resp.get_json()
    assert any(p["name"] == "Alice" for p in patients)