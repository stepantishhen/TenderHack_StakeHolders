from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from dashboard.models import *

from dashboard.forms import TicketForm


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


class TicketListView(generic.ListView):
    form_class = TicketForm
    success_url = "tickets"

    model = Ticket
    paginate_by = 10
    template_name = "dashboard/tickets.html"
    context_object_name = "ticket_list"

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return self.get(request)

# def tickets(request):
#     context = {
#         'form': TicketForm
#     }
#     return render(request, "dashboard/tickets.html", context=context)
