# clinic-legacy-system — Software Maintenance Plan

## 1. Project Overview
The *clinic-legacy-system* is a legacy clinic management web application built using *Python Flask*.  
The system suffers from maintainability issues such as duplicated logic, tight coupling, lack of validation, and limited testability.

This maintenance plan follows an *iterative sprint-based approach* to improve maintainability and introduce one controlled evolution change.

---

## 2. Maintenance Objectives
- Improve code maintainability and readability
- Reduce duplicated logic
- Add input validation and user feedback
- Reduce coupling between components
- Implement one evolution feature
- Add testing and regression control
- Evaluate improvements using software metrics
- Ensure no unintended behavior changes

---

## 3. Maintenance Scope

### In Scope
- Refactoring Flask routes and helper functions
- Improving patient and appointment handling
- Data model changes to reduce coupling
- Validation rules and UI feedback
- Automated and manual testing
- Documentation and metrics evaluation

### Out of Scope
- UI redesign
- Database migration
- Advanced security hardening

---

## 4. Team Roles (3 Members)

| Member | Responsibilities |
|-------|------------------|
| Member A | refactoring, duplication removal, repository cleanup |
| Member B | validation, error handling, testing |
| Member C | evolution feature, documentation, metrics evaluation |

All team members participate in code reviews, sprint retrospectives, and the final presentation.

---

## 5. Maintenance Backlog (User Stories)

### US-01 — Validate patient input  
As a clinic staff member, I want patient form inputs validated so incorrect or missing data cannot be submitted.

### US-02 — Validate appointment dates  
As a staff member, I want invalid appointment dates rejected to avoid scheduling errors.

### US-03 — Remove duplicated patient creation logic  
As a maintainer, I want duplicated helper logic unified so changes can be applied in one place.

### US-04 — Remove duplicated patient lookup logic  
As a maintainer, I want a single function for patient lookup to reduce inconsistencies.

### US-05 — Evolution: store patient_id in appointments instead of full object  
As a maintainer, I want appointment objects to reference only *patient_id* to reduce coupling.

### US-06 — Display validation and feedback messages  
As a clinic staff member, I want clear error messages shown in forms so I know what to fix.

---

## 6. Sprint-Based Maintenance Approach

This maintenance plan follows an *iterative sprint-based approach*.  
Each sprint represents a focused maintenance iteration with a clear goal, defined tasks, and measurable deliverables.

- *Sprint One:* Corrective and perfective maintenance (code cleanup and validation)
- *Sprint Two:* Evolutionary maintenance and metrics evaluation
- *Sprint Three:* Stabilization and regression testing
- *Sprint Four:* Preventive maintenance through documentation and code quality improvements
- *Sprint Five:* Final evaluation, reporting, and delivery

This approach ensures changes are incremental, controlled, and measurable.

---

## 7. Sprint Plan

### Sprint 1 (Week 3) — Refactoring + Validation

*What this sprint means:*  
Sprint One is the first maintenance iteration.  
Its purpose is to clean the legacy code, remove duplication, and correct structural issues *without changing system behavior*.

*Maintenance type:*  
Corrective + Perfective Maintenance

*Planned tasks:*
- Refactor duplicated helper functions (US-03, US-04)
- Improve separation of concerns
- Add patient input validation (US-01)
- Add appointment date validation (US-02)
- Display validation errors in forms (US-06)
- Update routes and templates accordingly

*Expected outcomes:*
- Reduced duplication
- Clearer responsibilities
- Safer input handling

---

### Sprint 2 (Week 4) — Evolution + Metrics

*What this sprint means:*  
Sprint Two introduces a controlled evolution change by modifying how appointments reference patients.

*Maintenance type:*  
Evolutionary + Perfective Maintenance

*Planned tasks:*
- Implement evolution change (US-05)
- Update appointment handling logic
- Remove unused or dead code
- Update patient delete logic if required
- Measure LOC, CC, and Maintainability Index
- Document refactoring results

*Expected outcomes:*
- Reduced coupling
- Clearer data model
- Measurable maintainability improvement

---

### Sprint 3 (Week 5) — Testing + Stabilization

*What this sprint means:*  
Sprint Three ensures that previous refactoring and evolution changes did not break existing functionality.

*Maintenance type:*  
Corrective + Preventive Maintenance

*Planned tasks:*
- Add unit tests for patient and appointment operations
- Run regression testing
- Fix detected defects
- Verify no behavior change
- Run automated tests using pytest -q
- Record and document test results

*Expected outcomes:*
- Improved system reliability
- Reduced regression risk
- Verified behavior stability

---

### Sprint 4 (Week 6) — Documentation + Code Quality

*What this sprint means:*  
Sprint Four focuses on improving long-term maintainability.

*Maintenance type:*  
Preventive Maintenance

*Planned tasks:*
- Improve naming and code readability
- Remove remaining technical debt
- Add docstrings and inline comments
- Update README.md
- Update refactor_log.md
- Re-evaluate maintainability metrics

*Expected outcomes:*
- Cleaner and more understandable codebase
- Improved long-term maintainability

---

### Sprint 5 (Week 7) — Final Evaluation + Delivery

*What this sprint means:*  
Sprint Five finalizes the maintenance lifecycle and prepares the project for submission.

*Maintenance type:*  
Perfective + Preventive Maintenance

*Planned tasks:*
- Compare before vs after metrics
- Finalize evaluation section
- Document lessons learned and challenges
- Identify future evolution opportunities
- Prepare presentation slides and demo
- Review Git commit history

*Expected outcomes:*
- Complete maintenance lifecycle
- Submission-ready repository and presentation

---

## 8. Sprint Deliverables Summary

| Sprint | Deliverables |
|-------|-------------|
| Sprint 1 | refactored code, validation, updated templates |
| Sprint 2 | evolution feature, metrics update |
| Sprint 3 | automated tests, regression results |
| Sprint 4 | documentation, code quality cleanup |
| Sprint 5 | final evaluation, presentation, demo |

---

## 9. Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| Regression bugs | incremental changes and frequent testing |
| Template breakage | staged updates and manual UI checks |
| Low test coverage | prioritize key flows and unit tests |

---

## 10. Conclusion

This plan demonstrates a complete software maintenance lifecycle covering *corrective, perfective, preventive, and evolutionary maintenance*, aligned with Software Maintenance & Evolution course objectives.