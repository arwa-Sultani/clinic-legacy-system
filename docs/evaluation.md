# Evaluation
- Metrics after: LOC, CC, MI
- Comparison before → after
- Tests run: `pytest -q` (paste output)
- Behavior changes (if any)
- Lessons/next steps
# Metrics & Evaluation (After Refactoring and Evolution)

## 1. Lines of Code (LOC)

The LOC was calculated *after refactoring and evolution* by counting all Python source files in the improved codebase.

### LOC Calculation

| Component              | Approx. LOC |
|------------------------|-------------|
| models/                | 45          |
| repositories/          | 85          |
| services/              | 110         |
| routes/                | 95          |
| utils/validation.py    | 35          |
| tests/                 | 70          |
| *Total LOC (After)*    | *440*       |

### Comparison

| Version            | LOC |
|--------            |-----|
| Before refactoring | ~275 |
| After refactoring  | ~440 |

*Observation:*  
The LOC increased by approximately *165 lines* due to:
- Modularization of the code
- Separation of concerns
- Addition of validation logic
- Introduction of automated tests  

This increase is acceptable and expected in maintainable systems.

---

## 2. Cyclomatic Complexity (CC)

Cyclomatic complexity was analyzed *qualitatively*.

### Before Refactoring:
- Large route functions handled multiple responsibilities.
- High number of conditional paths inside single functions.
- Estimated CC per main route: *8–10*.

### After Refactoring:
- Logic split across services and repositories.
- Smaller, focused functions.
- Estimated CC per function: *3–4*.

*Result:*  
Cyclomatic complexity per function was reduced by approximately *50–60%*.

---

## 3. Maintainability Index (MI)

Maintainability Index was evaluated qualitatively based on standard factors:
- LOC
- Complexity
- Readability
- Modularity
- Testability

### MI Comparison

| Factor | Before | After |
|------|--------|-------|
| Modularity | Low | High |
| Duplication | High | Low |
| Validation | Missing | Implemented |
| Test Coverage | None | Present |
| Maintainability | Low | High |

*Result:*  
The Maintainability Index increased significantly after refactoring and evolution.

---

## Tests Executed

Automated tests were executed after refactoring and evolution to verify system correctness.

Command used:
```bash
python -m pytest -q
Output:
2 passed in 0.19s
