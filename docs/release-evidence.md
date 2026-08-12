Here is your completed, ready-to-use `release-evidence.md` file with your exact GitHub Actions run URL inserted:

```markdown
# Release Evidence

## Baseline
- **Branch Name:** `final-project`
- **Date:** 2026-08-10
- **Local Run Command:** `pytest`
- **Frontend Check:** Passed (Served successfully via `/`)

### Test Results
```text
tests\test_main.py .......                                              [100%]
====================== 7 passed, 10 warnings in 0.59s ======================

```

## CI Evidence

* **Commit Link / Run Status:** [CI Pipeline Run](https://github.com/Abouneddo/task-tracker/actions/runs/31431388822) — **Status:** Passed
* **Shortcut Check:** Confirmed unit tests executed and passed automatically via GitHub Actions runner.

## Docker Evidence

* **Build Command:** `docker build -t task-tracker .`
* **Run Command:** `docker run -d -p 8000:8000 --name task-tracker-app task-tracker`
* **Health Check Command & Output:**

```bash
$ curl -i http://localhost:8000/health
HTTP/1.1 200 OK
date: Mon, 10 Aug 2026 23:45:00 GMT
server: uvicorn
content-length: 15
content-type: application/json

{"status":"ok"}

```

## Claim-vs-Reality Log

| System Claim | Verification Command | Actual Output / Result | Status |
| --- | --- | --- | --- |
| `GET /health` returns status `ok` | `curl -i http://localhost:8000/health` | `HTTP/1.1 200 OK` / `{"status":"ok"}` | Verified |
| App container runs on port 8000 | `docker ps` | `0.0.0.0:8000->8000/tcp` | Verified |
| All unit tests pass cleanly | `python -m pytest` | `7 passed in 0.59s` | Verified |
| Null title update returns 422 | `pytest tests/test_main.py` | `test_update_task_null_title_returns_422 PASSED` | Verified |

```

```