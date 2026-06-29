from app.extensions import db

class Order(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(
        db.Integer,
        primary_key = True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="PENDING"
    )

    total_amount = db.Column(
        db.Numeric(10,2),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # Relationships
    user = db.relationship(
        "User",
        back_populates="orders"
    )

    items = db.relationship(
        "OrderItem",
        back_populates="order",
        cascade="all,delete-orphan"
    )