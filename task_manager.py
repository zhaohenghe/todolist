import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            completed=data['completed']
        )

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks else []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            logging.info("No tasks found.")
            return

        for idx, task in enumerate(self.tasks):
            status = "✔️" if task.completed else "❌"
            logging.info(f"[{idx}] {task.title} ({task.due_date}) - {status}")
            logging.info(f"    {task.description}")

    def complete_task(self, index):
        try:
            self.tasks[index].completed = True
            logging.info(f"Marked task '{self.tasks[index].title}' as complete.")
        except IndexError:
            logging.info("Invalid task index.")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            logging.info(f"Deleted task '{removed.title}'.")
        except IndexError:
            logging.info("Invalid task index.")