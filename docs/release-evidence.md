```text
# Release Evidence

## Baseline Details
* **Test Command:** `python -m pytest`
* **Test Output:**
  ```text
  tests\test_main.py ......                                                [100%]
  ======================= 6 passed, 10 warnings in 0.56s =======================

```

## CI Evidence

* **Commit Link / Run Status:** [CI Pipeline Run](https://github.com/Abouneddo/task-tracker/actions/runs/31221770736) — **Status:** Passed
* **Shortcut Check:** Confirmed all 6 unit tests executed and passed automatically via GitHub Actions runner (`ubuntu-latest`, Python 3.11).

## Docker Evidence

* **Build Command:** `docker build -t task-tracker .`
* **Run Command:** `docker run -d -p 8000:8000 --name task-tracker-app task-tracker`
* **Health Check Command & Output:**
```bash
$ curl -i http://localhost:8000/health
HTTP/1.1 200 OK
date: Fri, 07 Aug 2026 22:03:11 GMT
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
| All unit tests pass cleanly | `python -m pytest` | `6 passed in 0.56s` | Verified |
