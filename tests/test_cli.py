import unittest
from unittest.mock import patch
from io import StringIO
import argparse  # Import argparse
from cli import main
from storage import save_tasks

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.test_file = 'tasks.json'
        save_tasks([], self.test_file)  

    def tearDown(self):
        save_tasks([], self.test_file) 

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='add', title='Task 1', description='Description 1', due='2025-05-10'))
    def test_add_task(self, mock_args, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Task 'Task 1' added.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='list'))
    def test_list_tasks_empty(self, mock_args, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("No tasks found.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='add', title='Task 1', description='Description 1', due='2025-05-10'))
    def test_list_tasks_with_tasks(self, mock_args, mock_stdout):
        # Add a task first
        main()
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='list')):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Task 1", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='complete', index=0))
    def test_complete_task(self, mock_args, mock_stdout):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                command='add', title='Task 1', description='Description 1', due='2025-05-10')):
            main()
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Marked task 'Task 1' as complete.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='delete', index=0))
    def test_delete_task(self, mock_args, mock_stdout):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                command='add', title='Task 1', description='Description 1', due='2025-05-10')):
            main()
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Deleted task 'Task 1'.", output)

if __name__ == '__main__':
    unittest.main()