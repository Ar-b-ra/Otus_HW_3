from queue import PriorityQueue
from typing import Callable

from custom_logger import root_logger


class Resolver:
    fifo_queue = PriorityQueue()

    def add_command(self, command: Callable):
        self.fifo_queue.put(command)

    def execute(self):
        try:
            command = self.fifo_queue.get()
        except Exception as exc:
            pass

    @staticmethod
    def put_to_log(exc: Exception, message: str):
        root_logger.critical(f"[{exc}]: {message}")
