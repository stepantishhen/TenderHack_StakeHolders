from django import forms
from django.forms import ModelForm

from dashboard.models import *

STATUS_CHOICE = [
    (1, 'отправлено'),
    (2, 'рассмотрено'),
    (3, 'решено'),
]


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["subject", "text", "performer", "initiator"]

    status = forms.CharField(
        widget=forms.Select(choices=STATUS_CHOICE),
    )