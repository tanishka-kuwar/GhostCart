from app.products.models import Product
from app.extensions import db

class ProductRepository:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def create_product(name,price,stock):
        product = Product(
            name = name,
            price = price,
            stock = stock
        )

        db.session.add(product)
        db.session.commit()

        return Product

    @staticmethod
    def update_product(product):

        db.session.commit()
        return product

    @staticmethod 
    def delete_product(product):

        db.session.delete(product)
        db.session.commit()