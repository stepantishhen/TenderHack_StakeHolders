from django.urls import path

from dashboard.views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
]