# Clinic Legacy System (Refactored / Modularized)

## Overview
A small Flask web app for managing patients and appointments. This repo demonstrates maintenance and refactoring of a legacy-like codebase toward a modular architecture.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the app
```bash
python app.py
```
Visit: http://127.0.0.1:5000

## Run tests
```bash
pytest -q
```

## Project structure
- `app.py` — app factory, wiring, blueprint registration
- `config.py` — configuration
- `routes/` — Flask blueprints (patients, appointments)
- `services/` — business logic
- `repositories/` — data access (currently in-memory)
- `models/` — domain models/dataclasses (optional)
- `utils/` — validation/helpers
- `templates/`, `static/` — UI assets
- `tests/` — pytest suites
- `docs/` — assignment deliverables (analysis, metrics, plan, evaluation)
- `refactor_log.md` — per-change notes

## Notes
- Data is in-memory by default. Restarting the app clears it.
- Replace placeholder validation/fields with your actual model needs.