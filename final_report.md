# Clinic Legacy System – Software Maintenance Final Report

## 1. Introduction
This report presents the software maintenance activities performed on the Clinic Legacy System.
The goal was to analyze a legacy codebase, apply refactoring techniques, implement one evolution change,
and evaluate the impact on maintainability.

---

## 2. System Overview
The system is a Flask-based web application that manages:
- Patients (add, edit, delete, list)
- Appointments (create and list)

Originally, the system stored all data in memory and used a monolithic structure.

---

## 3. Analysis Summary
The initial analysis identified several issues:
- High coupling and low cohesion
- Code duplication
- Missing input validation
- No automated tests
- Monolithic structure

An initial LOC of approximately 275 lines was recorded as a baseline.

---

## 4. Metrics & Estimation
After refactoring and evolution:
- LOC increased to approximately 440 lines due to modularization and testing.
- Cyclomatic Complexity per function decreased.
- Maintainability Index improved significantly.

These changes indicate better long-term maintainability despite the increase in LOC.

---

## 5. Maintenance Plan
The maintenance work was planned across two sprints:
- Sprint 1: Refactoring, validation, and modularization.
- Sprint 2: Evolution change, testing, and evaluation.

Tasks were distributed among team members focusing on services, routes, validation, and testing.

---

## 6. Refactoring & Evolution
Refactoring actions included:
- Separation into routes, services, repositories, models, and utilities.
- Removal of duplicated logic.
- Centralized input validation.

**Evolution Change Implemented:**
Appointments now reference patients using `patient_id` instead of embedding full patient objects.
This reduced coupling and improved data consistency.

---

## 7. Evaluation & Testing
Evaluation confirmed improvements in maintainability:
- Reduced coupling
- Improved cohesion
- Clear separation of concerns

Automated tests were executed using:
```bash
python -m pytest -q
