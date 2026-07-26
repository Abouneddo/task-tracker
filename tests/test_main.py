# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

# Single global TestClient instance
client = TestClient(app)

# Automatically clear database before and after each test run
@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    
    response = client.post("/tasks", json=payload)
    
    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["priority"] == "high"
    assert "id" in data

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    
    # Fixed: Status code is 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == yesterday
    assert data["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create one overdue task and one future task
    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    # Query overdue_only=true
    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    tasks = response.json()
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue"

# tests/test_main.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient

from app.main import app
from app.database import reset_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    reset_db()
    yield
    reset_db()

def test_create_task_baseline():
    payload = {
        "title": "Baseline Test Task",
        "description": "Verifying baseline setup",
        "priority": "high"
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201

def test_create_task_with_valid_due_date_and_overdue_check():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    response = client.post("/tasks", json={
        "title": "Past Due Task",
        "status": "todo",
        "due_date": yesterday
    })
    assert response.status_code == 201
    assert response.json()["is_overdue"] is True

def test_overdue_filter_query():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    client.post("/tasks", json={"title": "Overdue", "status": "todo", "due_date": yesterday})
    client.post("/tasks", json={"title": "Future", "status": "todo", "due_date": tomorrow})

    response = client.get("/tasks?overdue_only=true")
    assert response.status_code == 200
    assert len(response.json()) == 1

# --- NEW FEATURE 2 TESTS ---

def test_create_task_with_tags_validation():
    # Tests trimming, lowercasing, and duplicate removal
    response = client.post("/tasks", json={
        "title": "Tagged Task",
        "tags": ["  Urgent  ", "WORK", "urgent", "  dev  "]
    })
    assert response.status_code == 201
    data = response.json()
    # Expect cleaned list: ['urgent', 'work', 'dev']
    assert data["tags"] == ["urgent", "work", "dev"]

def test_reject_invalid_tags():
    # Case 1: Tag exceeds 20 characters
    res1 = client.post("/tasks", json={
        "title": "Long Tag Task",
        "tags": ["this-tag-is-way-too-long-for-validation"]
    })
    assert res1.status_code == 422  # Unprocessable Entity

    # Case 2: More than 5 tags
    res2 = client.post("/tasks", json={
        "title": "Too Many Tags",
        "tags": ["t1", "t2", "t3", "t4", "t5", "t6"]
    })
    assert res2.status_code == 422

def test_filter_tasks_by_tag():
    client.post("/tasks", json={"title": "Task A", "tags": ["frontend", "bug"]})
    client.post("/tasks", json={"title": "Task B", "tags": ["backend", "bug"]})
    client.post("/tasks", json={"title": "Task C", "tags": ["docs"]})

    # Query tag=frontend
    res = client.get("/tasks?tag=frontend")
    assert res.status_code == 200
    tasks = res.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task A"