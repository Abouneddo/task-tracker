# app/models.py
from datetime import date, datetime
from typing import List, Optional
from uuid import uuid4

class Task:
    def __init__(
        self, 
        title: str, 
        description: str = "", 
        status: str = "todo", 
        priority: str = "medium",
        due_date: Optional[date] = None,
        tags: Optional[List[str]] = None  # ADDED: Optional tags parameter
    ):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.status = status         # e.g., "todo", "in-progress", "done"
        self.priority = priority     # e.g., "low", "medium", "high"
        self.due_date = due_date     # Store as date object or ISO string/None
        self.tags = tags if tags is not None else []  # ADDED: Defaults to empty list
        self.created_at = datetime.utcnow().isoformat()

    def is_overdue(self) -> bool:
        """
        Returns True ONLY if due_date is set, it's before today's date, 
        and status is NOT 'done'.
        """
        if self.due_date and self.status != "done":
            # Handles if due_date was passed as string or date object
            due = date.fromisoformat(self.due_date) if isinstance(self.due_date, str) else self.due_date
            return due < date.today()
        return False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if isinstance(self.due_date, date) else self.due_date,
            "is_overdue": self.is_overdue(),
            "tags": self.tags,  # ADDED: Include tags list in dictionary serialization
            "created_at": self.created_at,
        }