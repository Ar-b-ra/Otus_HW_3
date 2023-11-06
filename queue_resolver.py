from queue import PriorityQueue
from typing import Callable

from custom_logger import root_logger


def resolve(exc: Exception):
    ExceptionHandler.resolve(exc)


class QueueWorker:
    fifo_queue = PriorityQueue()

    def add_command(self, command: Callable):
        self.fifo_queue.put(command)

    def execute(self):
        try:
            if self.fifo_queue.empty():
                return
            command = self.fifo_queue.get()
            command()
        except Exception as exc:
            ExceptionHandler().resolve(exc)

    def put_command(self, command: Callable):
        self.fifo_queue.put(command)


class ExceptionHandler:
    @staticmethod
    def put_exc_to_log(exc: Exception):
        root_logger.exception(f"[{type(exc)}]: {exc}")

    def resolve(self, exc: Exception):
        self.put_exc_to_log(exc)


