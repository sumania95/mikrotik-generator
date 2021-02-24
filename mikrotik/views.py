from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#JSON AJAX
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from .models import (
    Number_Ticket,
    Voucher,
    Mikrotik,
    User_Profile,
)

from .forms import Number_TicketForm
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

import routeros_api
import random
import string
from django.urls import reverse

class Generate(LoginRequiredMixin,TemplateView):
    template_name = 'mikrotik/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SUMANIA WIFI HOTSPOT"
        return context

def random_char(y):
       return ''.join(random.sample(string.ascii_uppercase,y))

class Generate_AJAXView(LoginRequiredMixin,View):
    template_name = 'mikrotik/forms.html'
    def get(self, request):
        data = dict()
        number_ticket = Number_TicketForm()
        context = {
            'number_ticket': number_ticket,
        }
        data['html_form'] = render_to_string(self.template_name,context)
        return JsonResponse(data)
    def post(self, request):
        data =  dict()
        if request.method == 'POST':
            mikrotik = Mikrotik.objects.first()
            try:
                connection = routeros_api.RouterOsApiPool(mikrotik.ip_address, username=mikrotik.username, password=mikrotik.password)
                api = connection.get_api()
                list_queues = api.get_resource('/ip/hotspot/user')
                number_ticket = Number_TicketForm(request.POST,request.FILES)
                if number_ticket.is_valid():
                    ticket = number_ticket.save()
                    number_ticket = Number_Ticket.objects.get(id=ticket.id)
                    user_profile = User_Profile.objects.get(id=number_ticket.user_profile_id)
                    for p in range(number_ticket.number_ticket):
                        string_random = random_char(5)
                        username = str(number_ticket.prefix)+str(string_random)
                        print(username)
                        list_queues.add(name=username, profile=user_profile.user_profile,limit_uptime=user_profile.uptime_limit)
                        Voucher.objects.create(number_ticket = number_ticket,username = username)
                    data['message_type'] = success
                    data['message_title'] = 'Successfully generated.'
                    data['url_print'] = reverse('voucher_print',kwargs={'pk':number_ticket.id})
            except Exception as e:
                data['message_type'] = error
                data['message_title'] = 'Connection '+ str(e)
        return JsonResponse(data)

class Voucher_Print(LoginRequiredMixin,View):
    def get(self, request,pk):
        ticket = Voucher.objects.filter(number_ticket_id = pk)
        context = {
            'ticket': ticket,
        }
        return render(request,'mikrotik/internet_ticket.html', context)
