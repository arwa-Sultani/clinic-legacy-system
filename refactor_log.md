sprint 1
step 1
 Merge duplicate patient creation functions
- What to change in app.py: Replace both add_patient_record and create_patient with a single function add_patient, and update all calls.

Step 2 — Update patient_add route in app.py
@app.route('/patients/add', methods=['GET','POST'])
def patient_add():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')
        # no validation, inconsistent types
        add_patient(name, age, phone)
        return redirect(url_for('list_patients'))
    return render_template('patient_add.html')
______________________________________________to 
@app.route('/patients/add', methods=['GET', 'POST'])
def patient_add():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        phone = request.form.get('phone', '').strip()

        if not name:
            return render_template('patient_add.html', error="Name is required", form={'name': name, 'age': age, 'phone': phone})
        if not age.isdigit():
            return render_template('patient_add.html', error="Age must be a whole number", form={'name': name, 'age': age, 'phone': phone})
        age_val = int(age)
        if age_val < 0 or age_val > 120:
            return render_template('patient_add.html', error="Age must be between 0 and 120", form={'name': name, 'age': age, 'phone': phone})
        if not phone:
            return render_template('patient_add.html', error="Phone is required", form={'name': name, 'age': age, 'phone': phone})

        add_patient(name, age_val, phone)
        return redirect(url_for('list_patients'))

    return render_template('patient_add.html', form={'name': '', 'age': '', 'phone': ''})
_____________________________________________________________________

## Step 3 — Improve Edit Patient validation + phone input format + preserve inputs (Corrective / Perfective)
**Problem (Before):**
- Editing a patient could accept invalid values (age letters, phone letters).
- When validation failed, the form returned old stored values, confusing the user.

**Change:**
- Applied the same validation rules in `/patients/<id>/edit` as in Add Patient.
- Added a flexible `PHONE_REGEX` to prevent letters in phone input (allows digits and symbols: `+ - / ( ) spaces`).
- Preserved user inputs on validation errors using a temporary patient object (`temp_patient`) sent to the template.

**Files changed:**
- `app.py` (`patient_edit` route + `PHONE_REGEX`)
- `templates/patient_edit.html`

**Result (After):**
- Invalid age/phone values are rejected.
- User sees the values they typed after an error (better UX).

**Evidence (Commit):**

---

## Step 4 — Remove duplicated patient lookup functions (Perfective Maintenance)
**Problem (Before):**
- Two helper functions (`find_patient` and `get_patient_by_id`) implemented identical logic to retrieve a patient by ID.
- This caused functional duplication and unnecessary maintenance overhead.

**Change:**
- Unified patient lookup logic into a single function `get_patient_by_id`.
- Replaced all usages of `find_patient(...)` with `get_patient_by_id(...)`.
- Removed the duplicated `find_patient` function.

**Files changed:**
- `app.py`

**Result (After):**
- Eliminated functional duplication.
- Improved maintainability by having a single source of truth for patient lookup.

**Evidence (Commit):**

---

## Step 5 — Improve Create Appointment: strict date + prevent past dates + preserve inputs (Corrective / Preventive)
**Problem (Before):**
- Appointment date accepted any text (e.g., `abcd`, `2025/12/20`) and even past dates.
- On error, user input was lost.

**Change:**
- Added strict server-side date validation:
  - Required field
  - Must match `YYYY-MM-DD`
  - Must be a real date (using `datetime.strptime`)
  - Must not be in the past (compared to `date.today()`)
- Preserved inputs on error using `form` (patient_id, date, description).
- Passed `today` to the template for UI constraint.

**Files changed:**
- `app.py` (`appointment_create` route)
- `templates/appointment_create.html`

**Result (After):**
- Invalid or past appointment dates are rejected with clear messages.
- User input remains in the form after errors.

**Evidence (Commit):**

---

## Step 6 — Make appointment description required (Corrective / Perfective)
**Problem (Before):**
- Appointment description could be empty, resulting in incomplete records.

**Change:**
- Made description required in the backend.
- Added the `required` attribute to the form input.

**Files changed:**
- `app.py` (`appointment_create` route)
- `templates/appointment_create.html`

**Result (After):**
- All appointments include a description, improving data completeness.

**Evidence (Commit):**

---

## Step 7 — Light UI improvements to templates (Perfective)
**Problem (Before):**
- Pages were minimally styled and inconsistent.

**Change:**
- Applied light, consistent styling (CSS) to templates:
  - `index.html`
  - `patients.html`
  - `appointments.html`
  - `patient_add.html`
  - `patient_edit.html`
  - `appointment_create.html`
- Improved layout, readability, and navigation.
- Kept all functionality unchanged.

**Files changed:**
- All templates listed above

**Result (After):**
- UI is clearer, more usable, and consistent.

**Evidence (Commit):**

---

## Sprint 1 Summary
- Removed duplication in patient creation and patient lookup helpers.
- Added robust validation for patient creation and editing.
- Prevented invalid phone formats and preserved user inputs on errors.
- Implemented strict appointment date validation and prevented past dates.
- Made appointment description mandatory.
- Improved UI consistency across all templates.


<!-- 

# Refactor Log
- Date:
- Change:
- Why:
- Files:
- Metrics (before/after if relevant):
- Tests run:
- Behavior changes: -->