import random
from datetime import datetime, timedelta

from app.extensions import db
from app.users.models import User
from app.products.models import Product
from app.orders.models import Order
from app.orders.order_item_model import OrderItem

def random_date():

    days = random.randint(0, 364)

    return datetime.now() - timedelta(days=days)

def seed_orders(order_count = 50000):
    print(f"Generating {order_count} orders...")

    users = User.query.all()
    products = Product.query.all()

    if not users or not products:
        print("Users or Products not found.")
        return

    processed = 0
    order_items = []

    for _ in range(order_count):

        user = random.choice(users)
        product = random.choice(products)
        quantity = random.randint(1,3)
        total = float(product.price)*quantity

        order = Order(
            user_id=user.user_id,
            total_amount=total,
            status="SUCCESS",
            created_at=random_date()
        )

        processed += 1
        db.session.add(order)
        db.session.flush()

        item = OrderItem(
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=quantity,
            price=product.price
        )

        order_items.append(item)

        # Commit every 1000 orders
        if len(order_items) % 1000 == 0:

            db.session.bulk_save_objects(order_items)
            db.session.commit()

            order_items.clear()

            print(f"{processed} orders processed...")

    if order_items:

        db.session.bulk_save_objects(order_items)
        db.session.commit()

    print("Orders generated successfully.")