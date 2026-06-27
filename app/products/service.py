from app.products.repository import ProductRepository

class ProductService:

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product(product_id):

        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def create_product(name,price,stock):
        return ProductRepository.create_product(
            name,
            price,
            stock
        )    

    @staticmethod
    def update_product(product , name, price,stock):
        product.name = name,
        product.price = price
        product.stock = stock

        return ProductRepository.update_product(product)

    @staticmethod
    def delete_product(product):
        ProductRepository.delete_product(product)