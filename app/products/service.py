from app.products.repository import ProductRepository

class ProductService:

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product(product_id):

        product = ProductRepository.get_product_by_id(product_id)

        if product is None:
            return None
        
        return product