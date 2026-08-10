# app/schemas.py
from datetime import date
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from fastapi import HTTPException, status

VALID_TRANSITIONS = {
    "todo": {"in_progress"},
    "in_progress": {"done", "todo"},
    "done": {"in_progress"},
}

def validate_status_transition(current_status: str, new_status: str) -> None:
    # 1. No change requested or missing status -> Do nothing
    if not new_status or current_status == new_status:
        return

    # 2. Check if new_status is in the allowed set for current_status
    allowed = VALID_TRANSITIONS.get(current_status, set())
    if new_status not in allowed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status transition from '{current_status}' to '{new_status}'."
        )

# Common fields shared across schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = "todo"
    priority: Optional[str] = "medium"
    due_date: Optional[date] = None  # Optional due date in YYYY-MM-DD format
    tags: List[str] = Field(default_factory=list)  # Default empty list for tags

    @field_validator('title')
    def validate_title_not_empty(cls, title: str):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or whitespace")
        return title.strip()

    @field_validator('tags')
    def validate_tags(cls, tags):
        if tags is None:
            return []
        cleaned_tags = []
        for tag in tags:
            stripped = tag.strip().lower()
            if not stripped or len(stripped) > 20:
                raise ValueError("Tags must be non-empty strings under 20 characters")
            if stripped not in cleaned_tags:
                cleaned_tags.append(stripped)
        if len(cleaned_tags) > 5:
            raise ValueError("Maximum 5 tags allowed per task")
        return cleaned_tags

# Payload required to create a new task
class TaskCreate(TaskBase):
    pass

# Payload allowed when updating a task (all fields optional)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[date] = None
    tags: Optional[List[str]] = None  # Optional tag updates

    @field_validator('title', mode='before')
    def validate_title_not_null(cls, v):
        # Catches explicit JSON payload: {"title": null}
        if v is None:
            raise ValueError("Title cannot be null")
        if isinstance(v, str) and not v.strip():
            raise ValueError("Title cannot be empty or whitespace")
        return v

    @field_validator('tags')
    def validate_tags(cls, tags):
        if tags is None:
            return tags
        cleaned_tags = []
        for tag in tags:
            stripped = tag.strip().lower()
            if not stripped or len(stripped) > 20:
                raise ValueError("Tags must be non-empty strings under 20 characters")
            if stripped not in cleaned_tags:
                cleaned_tags.append(stripped)
        if len(cleaned_tags) > 5:
            raise ValueError("Maximum 5 tags allowed per task")
        return cleaned_tags

# Response returned to client
class TaskResponse(TaskBase):
    id: str
    created_at: str
    is_overdue: bool = False

    model_config = ConfigDict(from_attributes=True)