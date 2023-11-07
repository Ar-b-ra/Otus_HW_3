import unittest
from queue import Queue

from custom_logger import root_logger
from queue_resolver import ExceptionHandler


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
        except Exception as exc:
            self.handler.resolve_execution(command)

        self.assertEqual(self.testing_queue.empty(), False)
        log_exception = self.testing_queue.get()
        with self.assertLogs(root_logger, level='INFO') as cm:
            log_exception()
            self.assertEqual(cm.records[0].getMessage(), "[<class 'Exception'>]: Raised exception")

        # Assert that the log message was written to the console correctly
        # You can use a library like `pytest` for more advanced assertions


if __name__ == '__main__':
    unittest.main()
