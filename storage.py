import json
import os
from task_manager import Task

def load_tasks(filepath='tasks.json'):
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, ValueError):
        return []

def save_tasks(tasks, filepath='tasks.json'):
    with open(filepath, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)