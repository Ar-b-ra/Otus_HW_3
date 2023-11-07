from queue import PriorityQueue

from queue_resolver import ExceptionHandler

if __name__ == "__main__":
    def exception_command():
        raise Exception("Raised exception")


    working_queue = PriorityQueue()
    resolver = ExceptionHandler(working_queue=working_queue)
    working_queue.put(exception_command)

    while not working_queue.empty():
        command = working_queue.get()
        try:
            command()
        except Exception as exc:
            resolver.resolve_execution(command=command)
