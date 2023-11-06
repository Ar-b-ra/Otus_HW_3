from queue_resolver import QueueWorker


if __name__ == "__main__":
    def exception_command():
        raise Exception("Raised exception")

    queue_worker = QueueWorker()
    queue_worker.add_command(exception_command)
    queue_worker.execute()
