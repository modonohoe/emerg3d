from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            custom_user = form.save()
            login(request, custom_user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {"form": form})
