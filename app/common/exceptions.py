class GhostCartException(Exception):
    pass

class ProductNotFoundError(GhostCartException):
    pass

class InsufficientStockError(GhostCartException):
    pass