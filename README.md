# Task Tracker Application

A lightweight FastAPI application for managing tasks, complete with tag filtering, due dates, and a Kanban board frontend.

---

## Local Setup & Development

### Prerequisites
* Python 3.11+
* Docker (optional, for containerized runs)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abouneddo/task-tracker.git
   cd task-tracker

```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## Final Project

Branch reviewed: `final-project`

### What this submission demonstrates

* Existing Task Tracker app still runs inside the intended course scope.


* CI runs the pytest suite on push and/or pull request.


* Docker image builds and runs with `/health` returning 200.


* AI review, security, and ownership evidence is in `docs/`.



### How to run locally

```bash
uvicorn app.main:app --reload

```

Access the backend API at `[http://127.0.0.1:8000](http://127.0.0.1:8000)` and the interactive docs at `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)`.

### How to run tests

```bash
python -m pytest

```

### How to run with Docker

```bash
# Build the Docker image
docker build -t task-tracker .

# Run the Docker container
docker run -d -p 8000:8000 --name task-tracker-app task-tracker

# Verify health endpoint
curl http://localhost:8000/health

```

### Evidence files

* `docs/release-evidence.md`

* `docs/final-ai-review.md`

* `docs/ai-playbook.md`


### AI assistance summary

* **AI helped draft or review:** CI workflow (`ci.yml`), Dockerfile, and evidence templates.


* **I verified the work by:** Running `python -m pytest`, manual `curl` testing on `/health`, and manual diff reviews.


* **One AI suggestion I rejected or corrected:** Refused an AI attempt to add full JWT authentication middleware since scope changes and new features were explicitly prohibited.



```

```