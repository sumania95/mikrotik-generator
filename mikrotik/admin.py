from django.contrib import admin

from .models import (
    User_Profile,
    Mikrotik,
    Number_Ticket,
    Voucher,
)


admin.site.register(User_Profile)
admin.site.register(Mikrotik)
admin.site.register(Number_Ticket)
admin.site.register(Voucher)
