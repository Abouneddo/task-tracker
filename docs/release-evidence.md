(venv) C:\Users\moham\OneDrive\Desktop\task-tracker>python -m pytest
============================================================= test session starts =============================================================
platform win32 -- Python 3.13.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\moham\OneDrive\Desktop\task-tracker
configfile: pyproject.toml
plugins: anyio-4.14.2
collected 6 items                                                                                                                              

tests\test_main.py ......                                                                                                                [100%]

============================================================== warnings summary ===============================================================
venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\moham\OneDrive\Desktop\task-tracker\venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

app\schemas.py:59
  C:\Users\moham\OneDrive\Desktop\task-tracker\app\schemas.py:59: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.13/migration/
    class TaskResponse(TaskBase):

tests/test_main.py::test_create_task_baseline
tests/test_main.py::test_create_task_with_valid_due_date_and_overdue_check
tests/test_main.py::test_overdue_filter_query
tests/test_main.py::test_overdue_filter_query
tests/test_main.py::test_create_task_with_tags_validation
tests/test_main.py::test_filter_tasks_by_tag
tests/test_main.py::test_filter_tasks_by_tag
tests/test_main.py::test_filter_tasks_by_tag
  C:\Users\moham\OneDrive\Desktop\task-tracker\app\models.py:23: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    self.created_at = datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================= 6 passed, 10 warnings in 1.59s ========================================================