import joblib
import pandas as pd
from datetime import datetime, timedelta

from app.products.models import Product

class DemandPredictor:

    model = joblib.load("app/ml/model.pkl")
    @staticmethod
    def predict_all():

        tomorrow = datetime.now() + timedelta(days=1)

        day = tomorrow.day
        month = tomorrow.month
        weekday = tomorrow.weekday()

        predictions = []

        products = Product.query.all()

        for product in products:

            X = pd.DataFrame([{
                "product_id": product.product_id,
                "day": day,
                "month": month,
                "weekday": weekday
            }])

            predicted_quantity = DemandPredictor.model.predict(X)[0]

            predictions.append({
                "product_id": product.product_id,
                "name": product.name,
                "predicted_quantity": round(predicted_quantity)
            })

        predictions.sort(
            key=lambda x: x["predicted_quantity"],
            reverse=True
        )

        return predictions