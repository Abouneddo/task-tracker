# Repository Guidelines & AI Directives

## Stack & Commands
* **Core Framework:** FastAPI
* **Testing Suite:** pytest (`python -m pytest`)
* **ASGI Server:** Uvicorn (`uvicorn app.main:app --reload`)
* **Containerization:** Docker (`docker build -t task-tracker .`)

## Guardrails
1. **Mandatory Documentation Check:** AI assistants and agents must read existing files in `docs/` before suggesting or implementing structural modifications.
2. **Protected Code Directories:** AI agents are strictly prohibited from modifying core business logic inside `app/` or interface components in `frontend/` without explicit maintainer approval.
3. **Validation Requirements:** Any code change proposed by an agent must maintain 100% pass rate on existing tests in `tests/`.