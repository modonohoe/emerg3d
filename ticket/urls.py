from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.create_enquiry_ticket, name='ticket'),
    path('thank-you/', views.thank_you, name='thank_you'),
]