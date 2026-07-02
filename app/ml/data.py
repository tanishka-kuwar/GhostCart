import pandas as pd

from app.extensions import db

from app.orders.models import Order
from app.orders.order_item_model import OrderItem
from app.products.models import Product


class TrainingData:

    @staticmethod
    def load():

        query = (
            db.session.query(
                Order.created_at,
                Product.product_id,
                Product.name,
                Product.category,
                OrderItem.quantity
            )
            .join(OrderItem, Order.order_id == OrderItem.order_id)
            .join(Product, Product.product_id == OrderItem.product_id)
        )

        rows = query.all()

        data = []

        for row in rows:

            data.append({

                "date": row.created_at.date(),

                "product_id": row.product_id,

                "product_name": row.name,

                "category": row.category,

                "quantity": row.quantity

            })

        return pd.DataFrame(data)