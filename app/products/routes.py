from flask import Blueprint,jsonify,request

from app.products.service import ProductService

products_bp = Blueprint(
    "products",
    __name__
)

def serialize(product):
    return{
        "id":product.product_id,
        "name":product.name,
        "price":float(product.price),
        "stock":product.stock,
    }

@products_bp.get("/products")
def get_products():

    products = ProductService.get_all_products()

    return jsonify([serialize(p) for p in products])

@products_bp.get("/products/<int:product_id>")
def get_product(product_id):
    product = ProductService.get_product(product_id)

    if not product:
        return jsonify({"message":"Product not found"}),404
    
    return jsonify(serialize(product))

@products_bp.post("/products")
def create_product():
    data = request.get_json()

    product = ProductService.create_product(
        data["name"],
        data["price"],
        data["stock"],
    )

    return jsonify(serialize(product)),201

@products_bp.put("/products/<int:product_id>")
def update_product(product_id):

    product = ProductService.get_product(product_id)

    if not product:
        return jsonify({"message":"Product not found"}),404

    data = request.get_json()

    ProductService.update_product(
        product,
        data["name"],
        data["price"],
        data["stock"],
    )

    return jsonify(serialize(product))

@products_bp.delete("/products/<int:product_id>")
def delete_product(product_id):

    product = ProductService.get_product(product_id)

    if not product:
        return jsonify({"message":"Product not found"}),404

    ProductService.delete_product(product)

    return jsonify({"message":"Deleted"})