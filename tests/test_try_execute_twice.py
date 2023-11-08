import unittest
from queue import Queue
from unittest.mock import Mock, patch

from custom_logger import root_logger
from exception_handler import ExceptionHandler


class TestTryAgainCommand(unittest.TestCase):

    def setUp(self):
        self.counter = 0
        self.testing_queue = Queue()
        self.handler = ExceptionHandler(self.testing_queue)

    def test_try_again_command_success(self):
        # Test when the command is executed successfully on the first try

        def try_execute_twice():
            self.counter += 1
            self.handler.try_again_command(try_execute_twice)
            self.assertEqual(self.counter, 1)

    def test_try_again_command_failure(self):
        # Test when the command is executed successfully on the first try

        def try_execute_twice():
            self.counter += 1
            if self.counter < 2:
                raise Exception("Raised exception")

            self.handler.try_again_command(try_execute_twice)
            self.assertTrue(self.testing_queue.empty())
            self.assertEqual(self.counter, 2)

    def test_try_again_command_exception(self):
        # Test when the command is executed successfully on the first try

        def try_execute_twice():
            self.counter += 1
            raise Exception("Raised exception")

        with self.assertLogs(root_logger, level='INFO') as cm:
            self.handler.try_again_command(try_execute_twice)
            write_to_log = self.testing_queue.get()
            write_to_log()
            self.assertEqual(cm.records[0].getMessage(), "[<class 'Exception'>]: Unresolved command: try_execute_twice")
            self.assertEqual(self.counter, 2)


if __name__ == '__main__':
    unittest.main()
