from datetime import date
from flask import Flask, request, redirect, url_for, render_template, jsonify
import datetime

app = Flask(__name__)

patients = []
appointments = []
_next_id = 1

import re
PHONE_REGEX = re.compile(r"^[0-9+\-\s()\/]{7,20}$")


def add_patient(name, age, phone):
    global _next_id, patients
    patient = {'id': _next_id, 'name': name, 'age': age, 'phone': phone, 'notes': ''}
    patients.append(patient)
    _next_id += 1
    return patient




def get_patient_by_id(pid): 
    for patient in patients:
        if patient['id'] == pid:
            return patient
    return None


@app.route('/')
def index():
    return render_template('index.html', patients=patients, appointments=appointments)

@app.route('/patients')
def list_patients():
    return render_template('patients.html', patients=patients)

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
            return render_template('patient_add.html', error="Phone is required",
                           form={'name': name, 'age': age, 'phone': phone})

        if not PHONE_REGEX.match(phone):
            return render_template('patient_add.html', error="Phone must be digits and allowed symbols (+ - / ( ) spaces)",
                           form={'name': name, 'age': age, 'phone': phone})


        add_patient(name, age_val, phone)
        return redirect(url_for('list_patients'))

    return render_template('patient_add.html', form={'name': '', 'age': '', 'phone': ''})

@app.route('/patients/<int:pid>/edit', methods=['GET', 'POST'])
def patient_edit(pid):
    p = get_patient_by_id(pid)
    if p is None:
        return "Not Found", 404

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        phone = request.form.get('phone', '').strip()

        temp_patient = {
            'id': p['id'],
            'name': name,
            'age': age,
            'phone': phone
        }

        if not name:
            return render_template('patient_edit.html', error="Name is required", patient=temp_patient)

        if not age.isdigit():
            return render_template('patient_edit.html', error="Age must be a whole number", patient=temp_patient)

        age_val = int(age)
        if age_val < 0 or age_val > 120:
            return render_template('patient_edit.html', error="Age must be between 0 and 120", patient=temp_patient)

        if not phone:
            return render_template('patient_edit.html', error="Phone is required", patient=temp_patient)

        if not PHONE_REGEX.match(phone):
            return render_template(
                'patient_edit.html',
                error="Phone must be digits and allowed symbols (+ - / ( ) spaces)",
                patient=temp_patient
            )

        p['name'] = name
        p['age'] = age_val
        p['phone'] = phone
        return redirect(url_for('list_patients'))

    return render_template('patient_edit.html', patient=p)



@app.route('/appointments')
def list_appointments():
    
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments/create', methods=['GET', 'POST'])
def appointment_create():
    if request.method == 'POST':
        patient_id_raw = (request.form.get('patient_id') or '').strip()
        date_in = (request.form.get('date') or '').strip()
        desc = (request.form.get('description') or '').strip()

        form = {'patient_id': patient_id_raw, 'date': date_in, 'description': desc}
        today_str = date.today().isoformat()

        try:
            pid = int(patient_id_raw)
        except ValueError:
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Invalid patient selected",
                                   form=form,
                                   today=today_str)

        patient = get_patient_by_id(pid)

        if not patient:
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Patient not found",
                                   form=form,
                                   today=today_str)

        if not date_in:
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Date is required (YYYY-MM-DD)",
                                   form=form,
                                   today=today_str)

        try:
            appt_date = datetime.datetime.strptime(date_in, "%Y-%m-%d").date()
        except ValueError:
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Invalid date format. Use YYYY-MM-DD",
                                   form=form,
                                   today=today_str)

        if appt_date < date.today():
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Appointment date cannot be in the past",
                                   form=form,
                                   today=today_str)
        
        if not desc:
            return render_template('appointment_create.html',
                                   patients=patients,
                                   error="Description is required",
                                   form=form,
                                   today=today_str)

        ap = {'id': len(appointments) + 1,
              'patient': patient,
              'date': date_in,
              'description': desc}
        appointments.append(ap)
        return redirect(url_for('list_appointments'))

    return render_template('appointment_create.html',
                           patients=patients,
                           form={'patient_id': '', 'date': '', 'description': ''},
                           today=date.today().isoformat())



@app.route('/api/patients', methods=['GET'])
def api_get_patients():
    return jsonify(patients)

@app.route('/api/appointments', methods=['GET'])
def api_get_appointments():
    return jsonify([{'id': a['id'], 'patient_id': a['patient']['id'], 'date': a['date'], 'description': a['description']} for a in appointments])

@app.route('/del_patient/<int:pid>')
def del_patient(pid):
    global patients, appointments
    
    newp = []
    for p in patients:
        if p['id'] != pid:
            newp.append(p)
    patients = newp
    newa = []
    for a in appointments:
        if a['patient']['id'] != pid:
            newa.append(a)
    appointments = newa
    return redirect(url_for('list_patients'))


def messy_maintenance_function(x):
   
    for p in patients:
        if p['age'] == '':
            p['age'] = None

    return len(patients) + len(appointments)


add_patient('Ahmed Ali', 30, '091-111-222')
add_patient('Sara Omar', 25, '092-222-333')
appointments.append({'id': 1, 'patient': patients[0], 'date': '2025-10-22', 'description': 'General Checkup'})

# changed the run pport to 5001
if __name__ == '__main__':
    app.run(debug=True, port=5001)