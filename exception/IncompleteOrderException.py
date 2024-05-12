class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order."):
        super().__init__(message)