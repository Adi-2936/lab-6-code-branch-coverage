# Lab 6 Password Policy Coverage Analysis

This repository is the completed Lab 6 work for the assigned `L6_L7_39_password_policy` project. It demonstrates statement and branch coverage with `pytest` and `coverage.py`.

## Final results

- Code coverage suite: 6 tests passed, 91% statement coverage
- Branch coverage suite: 17 tests passed, 100% statement and branch coverage
- Evidence: genuine screenshots captured from the real terminal sessions

## Setup

```bash
python -m pip install -r requirements.txt
cd lab6
```

## Code coverage command

```bash
coverage erase
coverage run --source=password_policy -m pytest -q CodeCoverageTest_39_password_policy.py
coverage report -m
```

## Branch coverage command

```bash
coverage erase
coverage run --branch --source=password_policy -m pytest -q BranchCoverageTest_39_password_policy.py
coverage report -m
```

The final report is available in `report/`.
