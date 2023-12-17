from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    # user attribute used in profile.html
    username = user.username
    email = user.email
    user_slug = user.slugify

    return render(request, 'profile.html', {
        'user': user,
        'username': username,
        'email': email,
        'user_slug': user_slug
    })