# clinic-legacy-system – Analysis (Week 1)

## 1. System Overview

This project is a small legacy *Flask-based* web application for a clinic.

It supports two main features:

- Managing *Patients* (add, edit, delete, list).
- Managing *Appointments* for patients (create and list).

All data is stored *in memory* using Python lists (patients and appointments) – there is no database, no authentication, and no automated tests. The application is mainly for educational/demo purposes.

---

## 2. Code Structure

The legacy codebase is very small and consists of:

- app.py  
  - Creates the Flask app.  
  - Defines global in-memory lists patients and appointments.  
  - Contains helper functions for creating and searching patients.  
  - Defines all Flask routes for patients and appointments.  
  - Seeds some initial data at the bottom of the file.  

- templates/  
  - index.html: Simple dashboard that shows lists of patients and appointments.  
  - patients.html: Table view listing all patients with edit/delete links.  
  - patient_add.html: Form to add a new patient.  
  - patient_edit.html: Form to edit an existing patient.  
  - appointments.html: List view of all appointments with a link to add a new one.  
  - appointment_create.html: Form to create a new appointment.

There is no explicit separation between *data layer, **business logic, and **presentation layer*. Most logic is inside app.py, and the templates are tightly coupled to the internal structure of the Python dictionaries.

---

## 3. Design and Code Issues

### 3.1 Coupling

- The templates directly access nested Python dictionaries  
  (e.g., a.patient.name, a.patient.id), which tightly couples the HTML views to the exact internal representation of appointments.
- The same file (app.py) is responsible for:
  - Data storage (lists of patients and appointments),
  - Business logic (creation, validation),
  - Web routing (Flask endpoints),
  - Seeding initial data.

*Conclusion:* the code shows *high coupling* between concerns (data, logic, and UI), which makes future changes harder.

---

### 3.2 Cohesion

- app.py has *low cohesion* because it mixes:
  - Helper functions,
  - Route handlers,
  - Data seeding,
  - A “maintenance” function messy_maintenance_function that modifies patients and returns a numeric value unrelated to the rest of the app.
- Some functions do more than one thing or have unclear responsibility, for example:
  - messy_maintenance_function both cleans internal data and computes a length value.

*Conclusion:* modules and functions are not clearly focused on a single responsibility.

---

### 3.3 Duplication

There is obvious code duplication in the legacy version:

- Two functions that create patients with almost identical logic:
  - add_patient_record(name, age, phone)
  - create_patient(name, age, phone)

- Two functions that search for patients by id:
  - find_patient(p_id)
  - get_patient_by_id(pid)

This duplication increases maintenance effort, because a change to the data structure must be repeated in multiple places.

---

### 3.4 Missing Validation and Error Handling

- patient_add and patient_edit routes accept form data *without validation*:
  - The name can be empty.
  - The age is stored as a raw string, not guaranteed to be numeric.
- appointment_create:
  - Accepts any date string without format checking.
  - Only checks if a patient exists, but does not validate other fields.
- When invalid input is provided, the application either fails silently or returns a plain error string instead of a proper user-friendly error message.

---

### 3.5 Missing Tests

- There are *no automated tests* (no unit tests and no integration tests).
- All testing must be done manually through the browser.
- This makes refactoring risky because there is no quick way to detect regressions.

---

### 3.6 Other Issues

- Global mutable state (patients, appointments, _next_id) is used throughout the file. This is acceptable for a small demo, but does not scale and is harder to reason about.
- Deleting a patient requires manually cleaning up appointments that reference that patient. This logic is implemented directly in the route using loops and temporary lists, which is error-prone.

---

## 4. Initial LOC (Lines of Code) Count

The lines of code were counted using the editor and a simple manual check of each file.  
The numbers below are approximate but good enough as a baseline.

| File                             | LOC (approx.) |
|----------------------------------|---------------|
| app.py                         | 150           |
| templates/index.html           | 20            |
| templates/patients.html        | 30            |
| templates/patient_add.html     | 15            |
| templates/patient_edit.html    | 15            |
| templates/appointments.html    | 25            |
| templates/appointment_create.html | 20         |
| *Total*                        | *275*       |

The exact numbers are not critical; what matters is having a baseline to compare against after refactoring and maintenance.