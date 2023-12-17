from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            custom_user = form.save()
            login(request, custom_user)
            return redirect(reverse('profile', kwargs={'slug': custom_user.slug}))
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {"form": form})


@login_required
def profile(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    return render(request, 'accounts/profile.html', {'user': user})
