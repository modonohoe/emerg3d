from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.create_enquiry_ticket, name='ticket'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('ticket/edit/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('ticket/delete/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
]