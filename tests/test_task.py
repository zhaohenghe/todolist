import unittest
from task_manager import Task

class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        task = Task("Test Task", "This is a test task.", "2025-05-10", False)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertEqual(task.due_date, "2025-05-10")
        self.assertFalse(task.completed)

    def test_to_dict(self):
        task = Task("Test Task", "This is a test task.", "2025-05-10", False)
        expected_dict = {
            'title': "Test Task",
            'description': "This is a test task.",
            'due_date': "2025-05-10",
            'completed': False
        }
        self.assertEqual(task.to_dict(), expected_dict)

    def test_from_dict(self):
        data = {
            'title': "Test Task",
            'description': "This is a test task.",
            'due_date': "2025-05-10",
            'completed': False
        }
        task = Task.from_dict(data)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertEqual(task.due_date, "2025-05-10")
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()