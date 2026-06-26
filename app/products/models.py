from app.extensions import db

class Product(db.Model):

    __tablename__ = "products"

    product_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    name =db.Column(
        db.String(255),
        nullable = False
    )

    price = db.Column(
        db.Numeric(10,2),
        nullable = False
    )

    stock = db.Column(
        db.Integer,
        nullable=False
    )

    reserved_stock = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        server_default = db.func.now()
    )

    def __repr__(self):
        return f"<Product {self.product_id}: {self.name}>"