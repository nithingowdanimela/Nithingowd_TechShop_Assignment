class AuthorizationException(Exception):
    def __init__(self, message="Authorization failed."):
        super().__init__(message)