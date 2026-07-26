# app/schemas.py
from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

# Common fields shared across schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = "todo"
    priority: Optional[str] = "medium"
    due_date: Optional[date] = None  # Optional due date in YYYY-MM-DD format
    tags: List[str] = Field(default_factory=list)  # ADDED: Default empty list for tags

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
    tags: Optional[List[str]] = None  # ADDED: Optional tag updates

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

# Response returned to client (includes id, creation timestamp, overdue status, and tags)
class TaskResponse(TaskBase):
    id: str
    created_at: str
    is_overdue: bool = False

    class Config:
        from_attributes = True