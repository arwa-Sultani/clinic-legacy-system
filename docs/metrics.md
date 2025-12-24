
# clinic-legacy-system – Metrics & Estimation (Week 1)

## 1. LOC Summary

We reuse the LOC values from the initial analysis as a simple size metric:

| File                              | LOC (approx.) |
|---------------------------------- |---------------|
| app.py                            | 128           |
| *Total*                           | *128*         |

LOC is only used as a rough indicator of project size and to compare before/after refactoring.

---

## 2. Approximate Function Point Analysis

Because this is a very small educational project, we use a simplified Function Point (FP) estimation.

### 2.1 External Inputs (EI)

User actions that send data into the system:

1. Add patient  
2. Edit patient  
3. Delete patient  
4. Create appointment  

We count *4 EIs* (low to average complexity).

### 2.2 External Outputs (EO)

Simple outputs or result screens:

1. Patients list  
2. Appointments list  
3. Dashboard view (combined view)  

We count *3 EOs* (low complexity).

### 2.3 External Inquiries (EQ)

Query-like operations:

- Dashboard view used as a simple inquiry of patients and appointments.

We count *1 EQ*.

### 2.4 Internal Logical Files (ILF) and External Interface Files (EIF)

- ILF: 2 (patients, appointments)
- EIF: 0 (no external files or systems)

Given the small scope and low complexity, we estimate the total Function Points as:

> *Estimated FP ≈ 22 FP* (around 20–25 FP).

This number is approximate and only used for comparison and COCOMO input.

---

## 3. COCOMO-Based Effort and Time Estimation

We apply the Basic COCOMO (Organic) model as a theoretical exercise.

### 3.1 Assumptions

- Total size: *KLOC ≈ 0.275* (275 LOC ≈ 0.275 KLOC)
- Development type: Organic (small, simple, in-house project)
- Standard COCOMO formulas:

Effort (person-months):  
> Effort = 2.4 × (KLOC)^1.05  

Time (months):  
> Time = 2.5 × (Effort)^0.38  

### 3.2 Calculations (approximate)

- Effort ≈ 2.4 × (0.275)^1.05 ≈ *0.62 person-months*
- Time   ≈ 2.5 × (0.62)^0.38 ≈ *2.1 months*

### 3.3 Interpretation for This Course Project

In reality, this is a student maintenance assignment:

- Work is done by a small team of 3 students.
- The project runs part-time over about 4–5 weeks.

So we interpret the COCOMO numbers as:

- Roughly *2–3 weeks of focused work* for one person,
- Which matches the planned schedule of two short sprints for analysis, refactoring, and evaluation.

The goal of this section is not precise prediction, but to demonstrate understanding of software size metrics and basic effort estimation.