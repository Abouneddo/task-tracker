# app/main.py
from datetime import date
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.staticfiles import StaticFiles
from typing import List, Optional

from app.database import tasks_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

app = FastAPI(title="Task Tracker API")

# Helper function to compute overdue status for dictionary tasks stored in tasks_db
def check_is_overdue(task_dict: dict) -> bool:
    due_date_str = task_dict.get("due_date")
    task_status = task_dict.get("status", "todo")
    
    if due_date_str and task_status != "done":
        due = date.fromisoformat(due_date_str) if isinstance(due_date_str, str) else due_date_str
        return due < date.today()
    return False

# --- CRUD Endpoints ---

# 1. Create a task
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    new_task = Task(
        title=task_in.title,
        description=task_in.description,
        status=task_in.status,
        priority=task_in.priority,
        due_date=task_in.due_date,
        tags=task_in.tags  # ADDED: Pass validated tags list to model
    )
    task_data = new_task.to_dict()
    tasks_db[new_task.id] = task_data
    return task_data

# 2. Get all tasks (supports overdue_only and tag filtering)
@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks(
    overdue_only: bool = Query(False),
    tag: Optional[str] = Query(None)  # ADDED: Tag query parameter
):
    tasks = []
    
    for task_data in tasks_db.values():
        # Ensure is_overdue state is freshly updated based on current date
        task_data["is_overdue"] = check_is_overdue(task_data)
        
        # Check overdue status
        if overdue_only and not task_data["is_overdue"]:
            continue
            
        # Check tag filtering (case-insensitive search against stored tags)
        if tag:
            task_tags = task_data.get("tags", [])
            if tag.lower() not in [t.lower() for t in task_tags]:
                continue
                
        tasks.append(task_data)
            
    return tasks

# 3. Update a task partially
@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task_in: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    stored_task = tasks_db[task_id]
    update_data = task_in.model_dump(exclude_unset=True)  # Only update fields sent in request
    
    # Handle converting date object to string if passed in update
    if "due_date" in update_data and isinstance(update_data["due_date"], date):
        update_data["due_date"] = update_data["due_date"].isoformat()
        
    stored_task.update(update_data)
    
    # Recalculate is_overdue after updating status or due_date
    stored_task["is_overdue"] = check_is_overdue(stored_task)
    
    tasks_db[task_id] = stored_task
    return stored_task

# 4. Delete a task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks_db[task_id]
    return None

# --- Static Files Mount ---
app.mount("/", StaticFiles(directory="static", html=True), name="static")