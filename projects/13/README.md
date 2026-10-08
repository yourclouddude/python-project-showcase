# Bookstore REST API

Build a persistent local FastAPI bookstore with server-generated IDs, separate input validation and deliberate HTTP outcomes.

## Implemented core
- Defines nonblank title/author, bounded Decimal price and forbids extra fields such as id.
- Uses SQLite persistence; price is represented as an exact string and availability as a JSON boolean.
- Generate IDs on creation, retain identity on update and return explicit status codes.

## Setup and run
From projects/13/ in this repository. Use Python 3.12 and a separate environment.

    python -m venv .venv
    # PowerShell
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux alternative
    source .venv/bin/activate
    python -m pip install -r requirements.txt

    python -m uvicorn main:app --host 127.0.0.1

## Expected result
Open http://127.0.0.1:8000/docs. POST sample_book.json: 201 with ID; restart and GET the same record.

## Important failure check
Negative prices and ID fields in the body return 422; missing records return 404; DELETE success returns 204.

## Optional extension
Add ownership-aware authorization, search/pagination, PostgreSQL and a container/CI deployment exercise.

## Learning evidence
Explain: Why should identity come from the path or server instead of an update body? Add one original requirement, a sample artifact and a short decision/test log. Credit any assistance and distinguish the supplied core from your own work.

## Boundaries and verification
The core has validated writes but no authentication/authorization and runs on 127.0.0.1. The optional protected-write extension must define users/ownership and test denied requests before public multi-user use. The documented /docs UI is a local development tool.

Runtime checked: Windows x64, Python 3.12.14, 8 October 2026. This project passed a clean dependency installation and an offline smoke scenario in its own environment; the selected-project regression suite is included at the repository root. The complete vault previously passed 52 regression checks. Other OS/Python and live-account branches are not verified. Use the README commands from the source folder, not a generic filename copied from another lesson.

## Official reference
[FastAPI request bodies](https://fastapi.tiangolo.com/tutorial/body/)
