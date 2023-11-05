import logging
from pathlib import Path


class ConsoleFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()


root_logger = logging.getLogger()

format_string = "%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s"
consoleFormatter = logging.Formatter(format_string)

filename = "logs.log"
filename = Path() / filename
consoleHandler = logging.StreamHandler()
consoleFormatter.default_time_format = '%Y-%m-%d %H:%M:%S'
consoleFormatter.default_msec_format = '%s.%03d'
consoleHandler.setFormatter(consoleFormatter)
root_logger.addHandler(consoleHandler)

root_logger.setLevel("DEBUG")

if __name__ == "__main__":
    root_logger.info("dasdsad")
