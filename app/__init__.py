from flask import Flask

from app.config import Config
from app.extensions import db,migrate
from app.products.models import Product
from app.products.routes import products_bp

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
    
    app.register_blueprint(products_bp)
    return app