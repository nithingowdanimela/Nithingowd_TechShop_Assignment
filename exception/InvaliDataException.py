class InvalidDataException(Exception):
    def __init__(self, message="Invalid data."):
        super().__init__(message)
