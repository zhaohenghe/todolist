import unittest
from unittest.mock import patch
from io import StringIO
import argparse
import logging
from cli import main
from storage import save_tasks

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.test_file = 'tasks.json'
        save_tasks([], self.test_file)
        # Configure logging to use StringIO
        self.log_stream = StringIO()
        self.log_handler = logging.StreamHandler(self.log_stream)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.INFO)

    def tearDown(self):
        save_tasks([], self.test_file)
        # Clean up logging
        logging.getLogger().removeHandler(self.log_handler)
        self.log_stream.close()

    def get_output(self):
        return self.log_stream.getvalue()

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='add', title='Task 1', description='Description 1', due='2025-05-10'))
    def test_add_task(self, mock_args):
        main()
        output = self.get_output()
        self.assertIn("Task 'Task 1' added.", output)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='list'))
    def test_list_tasks_empty(self, mock_args):
        main()
        output = self.get_output()
        self.assertIn("No tasks found.", output)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='add', title='Task 1', description='Description 1', due='2025-05-10'))
    def test_list_tasks_with_tasks(self, mock_args):
        main()
        self.log_stream.seek(0)
        self.log_stream.truncate()
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(command='list')):
            main()
        output = self.get_output()
        self.assertIn("Task 1", output)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='complete', index=0))
    def test_complete_task(self, mock_args):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                command='add', title='Task 1', description='Description 1', due='2025-05-10')):
            main()
        self.log_stream.seek(0)
        self.log_stream.truncate()
        main()
        output = self.get_output()
        self.assertIn("Marked task 'Task 1' as complete.", output)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        command='delete', index=0))
    def test_delete_task(self, mock_args):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                command='add', title='Task 1', description='Description 1', due='2025-05-10')):
            main()
        self.log_stream.seek(0)
        self.log_stream.truncate()
        main()
        output = self.get_output()
        self.assertIn("Deleted task 'Task 1'.", output)

if __name__ == '__main__':
    unittest.main()