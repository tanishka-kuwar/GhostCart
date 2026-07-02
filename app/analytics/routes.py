from flask import Blueprint
from flask import render_template

from app.analytics.service import AnalyticsService
from app.common.responses import success_response

analytics_bp = Blueprint(
    "analytics",
    __name__
)

@analytics_bp.get("/dashboard")
def dashboard():

    data = AnalyticsService.dashboard()

    return success_response(
        data,
        "Dashboard loaded successfully"
    )

@analytics_bp.get("/admin")
def admin_dashboard():

    data = AnalyticsService.dashboard()

    return render_template(
        "dashboard.html",
        dashboard=data
    )

@analytics_bp.get("/analytics/orders-chart")
def orders_chart():

    data = AnalyticsService.orders_chart()

    return success_response(
        data,
        "Orders chart loaded successfully"
    )

@analytics_bp.get("/analytics/low-stock")
def low_stock():

    alerts = AnalyticsService.low_stock_alerts()

    return success_response(
        alerts,
        "Low stock alerts loaded successfully"
    )

@analytics_bp.get("/analytics/predict")
def predict():

    data = AnalyticsService.demand_prediction()

    return success_response(
        data,
        "Prediction loaded successfully."
    )