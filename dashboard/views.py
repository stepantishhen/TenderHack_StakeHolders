from django.shortcuts import render
from django.views import generic

from dashboard.models import *


# Create your views here.

class Dashboard(generic.ListView):
    model = Ticket
    template_name = "dashboard/index.html"
    context_object_name = "global_info"


class LogListView(generic.ListView):
    model = SystemLog
    paginate_by = 1
    template_name = "dashboard/logs.html"
    context_object_name = "log_list"
