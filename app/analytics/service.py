from app.analytics.repository import AnalyticsRepository

class AnalyticsService:

    @staticmethod
    def dashboard():
        
        products = AnalyticsRepository.inventory()

        orders = AnalyticsRepository.recent_orders()

        inventory = []

        for product in products:
            inventory.append({
                "name":product.name,
                "stock": product.stock,
                "percentage": (product.stock / 200) * 100
            })

        return {
            "products": AnalyticsRepository.total_products(),
            "orders": AnalyticsRepository.total_orders(),
            "revenue": float(
                AnalyticsRepository.total_revenue()
            ),
            "inventory": inventory,
            "recent_orders":[{
                "order_id":order.order_id,
                "user_id":order.user_id,
                "amount":float(order.total_amount),
                "status":order.status,
                "created_at":(order.created_at.strftime("%d-%m-%Y %H:%M")
                                if order.created_at
                                else "N/A"
                                )

            }
            for order in orders
            ]
        }