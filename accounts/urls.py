from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import sign_up

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="accounts/login.html"), name='signin'),
    path('signup/', sign_up, name='signup'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
    # path('signout/', LogoutView.as_view(template_name="accounts/logout.html"), name='signout')
]
