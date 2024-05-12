class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency error."):
        super().__init__(message)