from django import forms
from django.forms import ModelForm
from .models import (
    Number_Ticket,
)

class Number_TicketForm(forms.ModelForm):
    class Meta:
        model = Number_Ticket
        fields = [
            'prefix',
            'number_ticket',
            'user_profile',
        ]
