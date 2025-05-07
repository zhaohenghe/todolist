import unittest
from task_manager import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Task 1")
        self.assertEqual(self.manager.tasks[0].description, "Description 1")
        self.assertEqual(self.manager.tasks[0].due_date, "2025-05-10")
        self.assertFalse(self.manager.tasks[0].completed)

    def test_list_tasks_empty(self):
        with self.assertLogs(level='INFO') as log:
            self.manager.list_tasks()
        self.assertIn("No tasks found.", log.output[0])

    def test_list_tasks(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        with self.assertLogs(level='INFO') as log:
            self.manager.list_tasks()
        self.assertIn("Task 1", log.output[0])

    def test_complete_task(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.manager.complete_task(0)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_complete_task_invalid_index(self):
        with self.assertLogs(level='INFO') as log:
            self.manager.complete_task(0)
        self.assertIn("Invalid task index.", log.output[0])

    def test_delete_task(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_delete_task_invalid_index(self):
        with self.assertLogs(level='INFO') as log:
            self.manager.delete_task(0)
        self.assertIn("Invalid task index.", log.output[0])

if __name__ == '__main__':
    unittest.main()