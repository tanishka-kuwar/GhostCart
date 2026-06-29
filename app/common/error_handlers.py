from app.common.exceptions import (
    ProductNotFoundError,
    InsufficientStockError,
)
from app.common.responses import error_response

def register_error_handler(app):

    @app.errorhandler(ProductNotFoundError)
    def product_not_found(error):
        return error_response("Product not found",404)


    @app.errorhandler(InsufficientStockError)
    def insufficient_stock(error):
        return error_response("Insufficient stock",408)

    @app.errorhandler(Exception)
    def internal_error(error):
        return error