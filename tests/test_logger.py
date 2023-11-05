import unittest
from custom_logger import root_logger


class RootLoggerTest(unittest.TestCase):
    def test_info(self):
        with self.assertLogs(root_logger, level='INFO') as cm:
            root_logger.info("Test message")
        # Assert that the log message was written to the console correctly
        # You can use a library like `pytest` for more advanced assertions


if __name__ == '__main__':
    unittest.main()
