# app/database.py

# In-memory dictionary to store tasks: { task_id (str): task_dict }
tasks_db = {}

def reset_db():
    """Clears all tasks from memory. Crucial for clean unit tests!"""
    global tasks_db
    tasks_db.clear()