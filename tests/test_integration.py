import unittest
import os
from ..task_manager import TaskManager, Task
from ..storage import load_tasks, save_tasks

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_tasks.json'
        self.manager = TaskManager()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_save_tasks(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.manager.add_task("Task 2", "Description 2", "2025-05-11")
        save_tasks(self.manager.tasks, self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(len(loaded_tasks), 2)
        self.assertEqual(loaded_tasks[0].title, "Task 1")
        self.assertEqual(loaded_tasks[1].description, "Description 2")

    def test_complete_task_and_save(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.manager.complete_task(0)
        save_tasks(self.manager.tasks, self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertTrue(loaded_tasks[0].completed)

    def test_delete_task_and_save(self):
        self.manager.add_task("Task 1", "Description 1", "2025-05-10")
        self.manager.add_task("Task 2", "Description 2", "2025-05-11")
        self.manager.delete_task(0)
        save_tasks(self.manager.tasks, self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].title, "Task 2")

    def test_load_empty_file(self):
        with open(self.test_file, 'w') as file:
            file.write('')
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(loaded_tasks, [])

    def test_save_and_load_empty_tasks(self):
        save_tasks([], self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(loaded_tasks, [])

    def test_load_invalid_json(self):
        with open(self.test_file, 'w') as file:
            file.write('invalid json')
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(loaded_tasks, [])

    def test_save_and_load_task_with_special_characters(self):
        self.manager.add_task("Task @#$", "Description with special chars: @#$%^&*", "2025-05-10")
        save_tasks(self.manager.tasks, self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].title, "Task @#$")
        self.assertEqual(loaded_tasks[0].description, "Description with special chars: @#$%^&*")

    def test_save_and_load_task_with_unicode(self):
        self.manager.add_task("Tâsk Üñîçødê", "Dëšçrïptïøñ", "2025-05-10")
        save_tasks(self.manager.tasks, self.test_file)
        loaded_tasks = load_tasks(self.test_file)
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].title, "Tâsk Üñîçødê")
        self.assertEqual(loaded_tasks[0].description, "Dëšçrïptïøñ")

if __name__ == '__main__':
    unittest.main()