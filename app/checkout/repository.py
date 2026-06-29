from app.extensions import db
from app.products.models import Product

from app.orders.models import Order
from app.orders.order_item_model import OrderItem

class CheckoutRepository:

    @staticmethod
    def get_product_for_update(product_id):
        """
        Lock the product row until the transaction complete
        """
        return (
            db.session.query(Product)
            .filter(Product.product_id == product_id)
            .with_for_update()
            .first()
        )

    @staticmethod
    def create_order(user_id,total_amount):
        order = Order(
            user_id=user_id,
            total_amount=total_amount,
            status="SUCCESS"
        )

        db.session.add(order)
        db.session.flush()

        return order

    @staticmethod
    def create_order_item(order_id,product_id,quantity,price):
        item = OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            price=price
        )

        db.session.add(item)
