#  Invoice Generator Web App

Generate a validated local invoice from a web form, with an escaped HTML preview and an in-memory ReportLab PDF download.

## Implemented core
- Validates text/quantity/rate and computes an exact Decimal total.
- Escapes paragraph text, wraps the service field and renders bytes into memory; no remote resource fetching.
- Uses a synchronous FastAPI route, which runs in a worker thread; preview and PDF are separate submissions/IDs.

## Setup and run
From projects/19/ in this repository. Use Python 3.12 and a separate environment.

    python -m venv .venv
    # PowerShell
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux alternative
    source .venv/bin/activate
    python -m pip install -r requirements.txt

    python -m uvicorn main:app --host 127.0.0.1

## Expected result
Open http://127.0.0.1:8000. Sample quantity 2 and rate 125.50 gives total 251.00 USD.

## Important failure check
Non-finite, negative or over-precision rates and invalid text/quantity return 422. PDF bytes are returned without accumulating temporary files.

## Optional extension
Add saved invoice history, multiple line items, tax rules and a queued renderer; WeasyPrint is an optional HTML-to-PDF alternative with native prerequisites.

## Learning evidence
Explain: Why must CPU-heavy rendering not run directly inside an async event loop? Add one original requirement, a sample artifact and a short decision/test log. Credit any assistance and distinguish the supplied core from your own work.

## Boundaries and verification
Local form demo: exact Decimal rate and quantity produce one line item, no tax/payment collection or stored invoice history. PDF uses ReportLab, while Jinja2 is the separate HTML preview. This is not an HTML-to-PDF engine. The synchronous route uses FastAPI’s worker thread; no queue is implemented. PDF bytes live in memory and no files accumulate.

Runtime checked: Windows x64, Python 3.12.14, 8 October 2026. This project passed a clean dependency installation and an offline smoke scenario in its own environment; the selected-project regression suite is included at the repository root. The complete vault previously passed 52 regression checks. Other OS/Python and live-account branches are not verified. Use the README commands from the source folder, not a generic filename copied from another lesson.

PDF uses ReportLab; Jinja2 renders a separate HTML preview. Native WeasyPrint setup is an optional extension, not a working fallback.

## Official reference
[FastAPI forms](https://fastapi.tiangolo.com/tutorial/request-forms/)


## Guided practice

See [PRACTICE.md](PRACTICE.md). Implement `practice_starter.py`, run `python practice_checks.py`, then compare `practice_reference.py` using `python practice_checks.py --reference`. The untouched starter intentionally fails until you implement it.
