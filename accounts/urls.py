from django.urls import path
from .views import sign_up, login_view, logout_view

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="accounts/login.html"), name='signin'),
    path('signup/', sign_up, name='signup')
    # path('signout/', LogoutView.as_view(template_name="accounts/logout.html"), name='signout')
]
