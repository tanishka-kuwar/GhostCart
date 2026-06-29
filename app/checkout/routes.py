from flask import Blueprint, request

from app.checkout.service import CheckoutService
from app.common.responses import success_response

checkout_bp = Blueprint("checkout", __name__)

@checkout_bp.post("/checkout")
def checkout():

    data = request.get_json()

    result = CheckoutService.checkout(
        user_id = data["user_id"],
        product_id = data["product_id"],
        quantity= data["quantity"]
    )

    if result["status"] == "SUCCESS":
        return success_response(
            result,
            "Order placed successfully",
            201
        )

    return success_response(
        result,
        result["message"],
        400
    )