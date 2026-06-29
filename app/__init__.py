from flask import Flask

from app.config import Config
from app.extensions import db,migrate

from app.products.models import Product
from app.products.routes import products_bp

from app.users.models import User

from app.orders.models import Order
from app.orders.order_item_model import OrderItem

from app.common.error_handlers import register_error_handler

from app.checkout.routes import checkout_bp

from app.analytics.routes import analytics_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return {
            "project":"GhostCart",
            "status":"Running"
        }
    
    register_error_handler(app)

    app.register_blueprint(products_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(analytics_bp)

    print(app.url_map)
    
    return app