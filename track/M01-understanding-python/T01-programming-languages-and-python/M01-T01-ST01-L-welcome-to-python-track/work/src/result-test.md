# Test Cases for `programming_vs_python.py`

## Program Logic Under Test
```python
percentage = int(input("enter the  percentage :"))
active_backlog = int(input("enter the backlog history :"))

if percentage >= 60 and active_backlog == 0:
    print("eligible")
else:
    print("not eligible")
```

---

## 4 Types of Test Cases (Truth Table / Decision Condition Testing)

| Test Case | Type / Scenario | Input: `percentage` | Input: `active_backlog` | Condition 1 (`>= 60`) | Condition 2 (`== 0`) | Expected Output | Actual Output | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **TC-01** | **Both True (Positive / Valid Case)** | 75 | 0 | True | True | `eligible` | `eligible` | **PASS** |
| **TC-02** | **True & False (Negative Case 1)** | 70 | 2 | True | False | `not eligible` | `not eligible` | **PASS** |
| **TC-03** | **False & True (Negative Case 2)** | 55 | 0 | False | True | `not eligible` | `not eligible` | **PASS** |
| **TC-04** | **Both False (Negative Case 3)** | 50 | 1 | False | False | `not eligible` | `not eligible` | **PASS** |

---

## Detailed Test Case Breakdown

### 1. Test Case 1: Both Conditions True (Positive / Happy Path)
- **Description:** Candidate meets both the percentage requirement ($\ge 60$) and has zero active backlogs.
- **Input:**
  - `percentage`: 75
  - `active_backlog`: 0
- **Evaluation:** `75 >= 60` (True) and `0 == 0` (True) $\rightarrow$ True
- **Expected Output:** `eligible`
- **Actual Output:** `eligible`
- **Result:** Pass

---

### 2. Test Case 2: Percentage Satisfied, Backlog Unsatisfied
- **Description:** Candidate has sufficient percentage ($\ge 60$) but has active backlogs.
- **Input:**
  - `percentage`: 70
  - `active_backlog`: 2
- **Evaluation:** `70 >= 60` (True) and `2 == 0` (False) $\rightarrow$ False
- **Expected Output:** `not eligible`
- **Actual Output:** `not eligible`
- **Result:** Pass

---

### 3. Test Case 3: Percentage Unsatisfied, Backlog Satisfied
- **Description:** Candidate has no active backlogs, but does not meet the minimum percentage criteria ($< 60$).
- **Input:**
  - `percentage`: 55
  - `active_backlog`: 0
- **Evaluation:** `55 >= 60` (False) and `0 == 0` (True) $\rightarrow$ False
- **Expected Output:** `not eligible`
- **Actual Output:** `not eligible`
- **Result:** Pass

---

### 4. Test Case 4: Both Conditions Unsatisfied
- **Description:** Candidate fails both the percentage requirement ($< 60$) and has active backlogs.
- **Input:**
  - `percentage`: 50
  - `active_backlog`: 1
- **Evaluation:** `50 >= 60` (False) and `1 == 0` (False) $\rightarrow$ False
- **Expected Output:** `not eligible`
- **Actual Output:** `not eligible`
- **Result:** Pass

---

## Boundary Value Test Cases (Edge Cases)

| Test Case | Scenario | Input: `percentage` | Input: `active_backlog` | Expected Output | Actual Output | Status |
| :---: | :--- | :---: | :---: | :--- | :--- | :---: |
| **BVC-01** | Exact cutoff boundary | 60 | 0 | `eligible` | `eligible` | **PASS** |
| **BVC-02** | Just below cutoff boundary | 59 | 0 | `not eligible` | `not eligible` | **PASS** |
