class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock."):
        super().__init__(message)