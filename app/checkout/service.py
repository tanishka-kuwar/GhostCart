from app.extensions import db
from app.checkout.repository import CheckoutRepository
from app.common.logger import logger

class CheckoutService:

    @staticmethod
    def checkout(user_id,product_id, quantity):

        try:

            logger.info(
            f"Checkout started | user={user_id} product={product_id} quantity={quantity}")

            # Begin Tranction
            product = CheckoutRepository.get_product_for_update(product_id)

            if product is None:
                db.session.rollback()

                return{
                    "status":"FAILED",
                    "message":"Product not found"
                }
            
            logger.info(
            f"Product locked | product_id={product.product_id}")

            if product.stock < quantity:
                db.session.rollback()

                return{
                    "status":"FAILED",
                    "message":"Insufficient stock"
                }

            total = float(product.price)*quantity

            product.stock -= quantity

            order = CheckoutRepository.create_order(
                user_id=user_id,
                total_amount=total
            )

            CheckoutRepository.create_order_item(
                order.order_id,
                product.product_id,
                quantity,
                product.price
            )

            db.session.commit()

            logger.info(
            f"Committing transaction | order_id={order.order_id}")

            return {
                "status":"SUCCESS",
                "order_id":order.order_id
            }

        except Exception as e:

            db.session.rollback()

            logger.exception("Checkout failed")

            return {
                "status":"FAILED",
                "message":str(e)
            }