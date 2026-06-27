from flask import Blueprint,jsonify

from app.products.service import ProductService

products_bp = Blueprint(
    "products",
    __name__
)

@products_bp.route("/products",methods=["GET"])
def get_products():
    products = ProductService.get_all_products()

    result = []

    for product in products:
        result.append({
            "id": product.product_id,
            "name":product.name,
            "price":float(product.price),
            "stock":product.stock
        })

    return jsonify(result),200