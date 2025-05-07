import unittest
import os
import json
from storage import load_tasks, save_tasks
from task_manager import Task

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_tasks.json'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_tasks_empty_file(self):
        with open(self.test_file, 'w') as file:
            file.write('')
        tasks = load_tasks(self.test_file)
        self.assertEqual(tasks, [])

    def test_load_tasks_invalid_json(self):
        with open(self.test_file, 'w') as file:
            file.write('invalid json')
        tasks = load_tasks(self.test_file)
        self.assertEqual(tasks, [])

    def test_load_tasks_valid_json(self):
        data = [
            {'title': 'Task 1', 'description': 'Description 1', 'due_date': '2025-05-10', 'completed': False},
            {'title': 'Task 2', 'description': 'Description 2', 'due_date': '2025-05-11', 'completed': True}
        ]
        with open(self.test_file, 'w') as file:
            json.dump(data, file)
        tasks = load_tasks(self.test_file)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, 'Task 1')
        self.assertEqual(tasks[1].completed, True)

    def test_save_tasks(self):
        tasks = [
            Task('Task 1', 'Description 1', '2025-05-10', False),
            Task('Task 2', 'Description 2', '2025-05-11', True)
        ]
        save_tasks(tasks, self.test_file)
        with open(self.test_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['title'], 'Task 1')
        self.assertEqual(data[1]['completed'], True)

if __name__ == '__main__':
    unittest.main()