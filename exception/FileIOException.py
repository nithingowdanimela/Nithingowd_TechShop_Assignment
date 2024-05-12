class FileIOException(Exception):
    def __init__(self, message="File I/O error."):
        super().__init__(message)