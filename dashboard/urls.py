from django.urls import path

from dashboard.views import *

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("tickets/", TicketListView.as_view(), name="tickets"),
    path("logs/", LogListView.as_view(), name="logs")
]