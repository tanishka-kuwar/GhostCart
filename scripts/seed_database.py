from faker import Faker
import random

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app
from app.extensions import db
from app.products.models import Product
from app.orders.order_item_model import OrderItem
from app.orders.models import Order
from app.users.models import User

from scripts.catalog import PRODUCT_CATALOG
from scripts.utils import (
    get_variants,
    generate_sku,
    generate_stock,
    PRICE_INCREMENT
)
from scripts.users import seed_users
from scripts.orders import seed_orders

fake = Faker()

app = create_app()

print("="*50)
print("GhostCart Database Seeder")
print("="*50)

def build_product_catalog():

    catalog = []

    for brand, categories in PRODUCT_CATALOG.items():

        for category, products in categories.items():

            variants = get_variants(category)

            for product_name, base_price in products:

                for variant in variants:

                    final_name = product_name

                    if variant:
                        final_name += f" ({variant})"

                    catalog.append({

                        "brand": brand,

                        "category": category,

                        "name": final_name,

                        "sku": generate_sku(
                            brand,
                            product_name,
                            variant
                        ),

                        "price": base_price + PRICE_INCREMENT[variant],

                        "stock": generate_stock()

                    })

    return catalog

catalog = build_product_catalog()

with app.app_context():

    print("Cleaning database...")

    OrderItem.query.delete()
    Order.query.delete()
    Product.query.delete()
    User.query.delete()

    db.session.commit()

    print("Database cleaned successfully.")

with app.app_context():
    seed_users(1000)

with app.app_context():

    print(f"Inserting {len(catalog)} products...")

    products = []

    for item in catalog:

        product = Product(
            name=item["name"],
            brand=item["brand"],
            category=item["category"],
            sku=item["sku"],
            price=item["price"],
            stock=item["stock"],
            reserved_stock=0
        )

        products.append(product)

    db.session.bulk_save_objects(products)
    db.session.commit()

    print(f"Inserted {len(products)} products.")

with app.app_context():
    seed_orders(50000)

print(f"Generated {len(catalog)} products")