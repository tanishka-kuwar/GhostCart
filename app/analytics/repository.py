from sqlalchemy import func

from app.extensions import db
from app.products.models import Product
from app.orders.models import Order

class AnalyticsRepository:
    
    @staticmethod
    def total_products():
        return Product.query.count()

    @staticmethod
    def total_orders():
        return Order.query.count()

    @staticmethod
    def total_revenue():
        revenue = db.session.query(
            func.sum(Order.total_amount)
        ).scalar()

        return revenue or 0

    @staticmethod
    def inventory():
        return Product.query.all()

    @staticmethod
    def recent_orders(limit=10):

        return(
            Order.query
            .order_by(Order.order_id.desc())
            .limit(limit)
            .all()
        )