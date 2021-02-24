from django.urls import path,include
from .import views

from .views import (
    Generate,
    Generate_AJAXView,
    Voucher_Print,
)

urlpatterns = [
    path('', Generate.as_view(), name = 'base'),
    path('api/form', Generate_AJAXView.as_view(), name = 'base_form'),
    path('voucher/<int:pk>', Voucher_Print.as_view(), name = 'voucher_print'),
]
