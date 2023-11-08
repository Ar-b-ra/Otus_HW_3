import unittest
from queue import Queue

from custom_logger import root_logger
from exception_handler import ExceptionHandler


class ExceptionHandlerTest(unittest.TestCase):

    def setUp(self):
        self.testing_queue = Queue()
        self.handler = ExceptionHandler(self.testing_queue)

    def test_put_command(self):
        def exception_command():
            raise Exception("Raised exception")

        self.testing_queue.put(exception_command)
        command = self.testing_queue.get()
        try:
            command()
        except Exception as _:
            self.handler.resolve_execution(command)

        self.assertFalse(self.testing_queue.empty())
        log_exception = self.testing_queue.get()
        with self.assertLogs(root_logger, level='INFO') as cm:
            log_exception()
            self.assertEqual(cm.records[0].getMessage(), "[<class 'Exception'>]: Raised exception")

        # Assert that the log message was written to the console correctly
        # You can use a library like `pytest` for more advanced assertions

    def test_resolve_execution(self):
        def exception_command():
            raise Exception("Raised exception")

        with self.assertLogs(root_logger, level='INFO') as cm:
            self.handler.resolve_execution(exception_command)
            self.assertEqual(cm.records[0].getMessage(), "Resolving command: exception_command")
            log_command = self.testing_queue.get()
            log_command()
            self.assertEqual(cm.records[1].getMessage(), "[<class 'Exception'>]: Raised exception")
            self.assertEqual(len(cm.records), 2)
            self.assertFalse(self.testing_queue.empty())


if __name__ == '__main__':
    unittest.main()
