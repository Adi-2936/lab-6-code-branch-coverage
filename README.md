# Lab 6 Code and Branch Coverage Analysis

This repository demonstrates the difference between line coverage and branch coverage with a small Python discount calculator.

## Files

- `calculator_application.py` - application under test
- `CodeCoverageTest_student_application.py` - line-coverage suite
- `BranchCoverageTest_student_application.py` - branch-coverage suite
- `evidence/` - final coverage screenshots
- `report/` - final lab report

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run line coverage

```bash
coverage erase
coverage run --source=calculator_application -m pytest -q CodeCoverageTest_student_application.py
coverage report -m
```

## Run branch coverage

```bash
coverage erase
coverage run --branch --source=calculator_application -m pytest -q BranchCoverageTest_student_application.py
coverage report -m
```

Both final suites exceed the lab requirement of 90% coverage. The line suite reaches 100% statement coverage, while the branch suite reaches 100% statement and branch coverage.
