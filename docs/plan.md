# Plan
- Roles (3 people)
- Backlog/user stories (patients, appointments, remove globals, add validation, tests, evolution feature)
- Sprint 1: modularize, remove globals, validation, smoke tests
- Sprint 2: evolution feature, more tests, docs, metrics updates
# clinic-legacy-system – Maintenance Plan (Week 2)

## 1. Project Maintenance Goals

The legacy Flask clinic system shows several maintainability issues:
- duplicated logic
- lack of validation
- unclear responsibilities
- missing testability
- tightly coupled UI and backend logic

The maintenance objective for this project:
- improve maintainability
- refactor duplicated logic
- improve data validation
- reduce coupling
- restructure code for clarity
- implement one evolution change

---

## 2. Backlog – Proposed User Stories

The following user stories represent system improvements from a maintenance perspective.

### US-01 – Validate patient input
> As a clinic staff member, I want patient form inputs to be validated so that incorrect or missing data cannot be submitted.

### US-02 – Validate appointment dates
> As a staff member, I want invalid appointment dates rejected so that schedule errors are avoided.

### US-03 – Remove duplicated patient creation logic
> As a maintainer, I want to unify helper functions so changes can be applied in one place.

### US-04 – Remove duplicated patient lookup logic
> As a maintainer, I want a single function for finding a patient by id to reduce inconsistencies.

### US-05 – Store appointment reference as patient_id instead of full object
> As a maintainer, I want appointment objects to reference patient_id only, reducing coupling between components.

### US-06 – Display validation errors and feedback messages
> As a clinic staff member, I want clear error messages displayed in forms so I know what to correct.

---

## 3. Sprint Plan (2 Sprints)

We plan to deliver the maintenance tasks across two short iterations.

### Sprint 1 (Week 3)
Focus: refactoring + validation

Planned tasks:
- refactor duplicate functions (US-03, US-04)
- add input validation for patients (US-01)
- add date validation for appointments (US-02)
- display form errors (US-06)
- update templates to show error messages
- update routing logic accordingly

Expected outcomes:
- reduced code duplication
- better cohesion and clarity
- more reliable input handling

---

### Sprint 2 (Week 4)
Focus: evolution + cleanup

Planned tasks:
- implement evolution change (US-05: store patient_id instead of full patient object in appointments list)
- remove dead/unused code
- update delete logic for patients
- re-evaluate LOC + maintainability metrics
- document refactoring changes (refactor_log.md)
- update evaluation and test notes

Expected outcomes:
- improved maintainability
- lower coupling between models
- clearer data model
- measurable LOC improvements

---

## 4. Team Assignments (3 Members)

| Member | Responsibilities |
|--------|------------------|
| *Member A* | refactor duplicated functions + repository cleanup |
| *Member B* | implement patient + appointment input validation + error handling |
| *Member C* | evolution task (patient_id reference), update delete logic, documentation |

All members collaborate on:
- code review
- evaluation and sprint retrospective
- preparing final demo and report

---

## 5. Risk Notes

- refactoring without automated tests increases risk of regressions  
- changes to data references may break templates  
- manual testing effort may increase during sprints  

Mitigation strategies:
- incremental refactoring
- frequent manual checks
- code walkthrough sessions among team members

---

## 6. Deliverables for Each Sprint

| Sprint | Deliverables |
|--------|-------------|
| Sprint 1 | refactored helpers + improved form validation + updated templates |
| Sprint 2 | evolution implementation + updated documentation + LOC + evaluation |