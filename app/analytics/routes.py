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