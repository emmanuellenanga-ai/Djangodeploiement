from django.urls import path, include
from dashboard.views import dashboard_stats

urlpatterns = [
    path('stats/',dashboard_stats)
]