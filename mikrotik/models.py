from django.db import models
from django.db.models import Model, ForeignKey

class User_Profile(models.Model):
    user_profile = models.CharField(max_length = 200,unique=True)
    uptime_limit = models.CharField(max_length = 200)
    amount = models.IntegerField(default = 5)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.user_profile)

class Number_Ticket(models.Model):
    prefix = models.CharField(max_length = 2)
    number_ticket = models.IntegerField(default = 30)
    user_profile = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.number_ticket)

class Voucher(models.Model):
    number_ticket = models.ForeignKey(Number_Ticket, on_delete=models.CASCADE)
    username = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.voucher)

class Mikrotik(models.Model):
    ip_address = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.ip_address)
