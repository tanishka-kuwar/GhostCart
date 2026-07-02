from app.analytics.repository import AnalyticsRepository
from app.ml.predictor import DemandPredictor

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
            "revenue": float(AnalyticsRepository.total_revenue()),
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

            } for order in orders],
            "alerts": AnalyticsService.low_stock_alerts(),
            "predictions": AnalyticsService.demand_prediction()[:5]
        }
    
    @staticmethod
    def orders_chart():

        data = AnalyticsRepository.orders_per_day()

        labels = []
        values = []

        for day, count in data:

            labels.append(day.strftime("%d-%b"))

            values.append(count)

        return {
            "labels": labels,
            "values": values
        }

    @staticmethod
    def low_stock_alerts():

        products = AnalyticsRepository.low_stock_products()

        alerts = []

        for product in products:

            if product.stock == 0:
                status = "OUT OF STOCK"
                color = "danger"

            elif product.stock <= 20:
                status = "LOW STOCK"
                color = "warning"

            else:
                status = "HEALTHY"
                color = "success"

            alerts.append({

                "name": product.name,

                "stock": product.stock,

                "status": status,

                "color": color

            })

        return alerts

    @staticmethod
    def demand_prediction():

        return DemandPredictor.predict_all()