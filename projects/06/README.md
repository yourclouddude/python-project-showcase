# Expense Tracker (CSV)

Track expenses in UTF-8 CSV using Decimal amounts, category totals and explicit invalid-row reporting.

## Implemented core
- Rejects invalid money values and normalizes to two decimal places.
- Appends a dated record and writes a header for a new file.
- Reports invalid line numbers and aggregates valid rows by category, optionally by month.

## Setup and run
From projects/06/ in this repository. Use Python 3.12 and a separate environment.

    python -m venv .venv
    # PowerShell
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux alternative
    source .venv/bin/activate
    python -m pip install -r requirements.txt

    python main.py --file sample_expenses.csv
    python main.py --file expenses.csv --add 2.50 Food

## Expected result
The sample totals 19.75; row 4 containing nan is reported and skipped.

## Important failure check
Negative, non-finite and over-precision amounts are rejected; a wrong CSV header stops the operation.

## Optional extension
Add monthly budgets and a chart based on cleaned rows.

## Learning evidence
Explain: Why construct Decimal from text rather than a binary float? Add one original requirement, a sample artifact and a short decision/test log. Credit any assistance and distinguish the supplied core from your own work.

## Boundaries and verification
The supplied core is local. It does not require account access, deployment or paid services.

Runtime checked: Windows x64, Python 3.12.14, 8 October 2026. This project passed a clean dependency installation and an offline smoke scenario in its own environment; the selected-project regression suite is included at the repository root. The complete vault previously passed 52 regression checks. Other OS/Python and live-account branches are not verified. Use the README commands from the source folder, not a generic filename copied from another lesson.

## Official reference
[Python Decimal](https://docs.python.org/3/library/decimal.html)


## Guided practice

See [PRACTICE.md](PRACTICE.md). Implement `practice_starter.py`, run `python practice_checks.py`, then compare `practice_reference.py` using `python practice_checks.py --reference`. The untouched starter intentionally fails until you implement it.
