from django.urls import path, include, reverse
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import sign_up, profile

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="accounts/login.html"), name='signin'),
    path('signup/', sign_up, name='signup'),
    path('profile/<slug:slug>/', profile, name='profile'),
    path('logout/', LogoutView.as_view, name='logout'),
    path('logout_confirmation/', TemplateView.as_view(template_name='logout_confirmation.html'), name='logout_confirmation')
]
