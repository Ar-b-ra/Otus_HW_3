from queue import Queue
from typing import Callable

from custom_logger import root_logger


def log_exception(exc):
    # Записывает информацию о выброшенном исключении в лог (п.4)
    root_logger.exception(f"[{type(exc)}]: {exc}")


class ExceptionHandler:
    def __init__(self, working_queue: Queue = None):
        self.working_queue = working_queue
        self.unresolved_commands = dict()

    def put_command_to_queue(self, command):
        self.working_queue.put(command)

    def put_exc_to_log(self, exc):
        # Кладёт в очередь запись ошибки команды в лог (п. 5)
        self.put_command_to_queue(lambda: log_exception(exc))

    def resolve_execution(self, command: Callable):
        # Отправляет команду на выполнение после первой неудачной попытки (п. 6, 7, 8)
        self.unresolved_commands[command.__name__] = command
        root_logger.info(f"Resolving command: {command.__name__}")
        try:
            command()
        except Exception as exc:
            self.put_exc_to_log(exc)
            self.working_queue.put(lambda: self.try_again_command(command))

    def try_again_command(self, command: Callable):
        # Отправляет команду на выполнение после второй неудачной попытки (п. 8, 9)
        try:
            command()
        except Exception as _:
            try:
                command()
            except Exception as exc:
                self.put_exc_to_log(Exception(f"Unresolved command: {command.__name__}"))
