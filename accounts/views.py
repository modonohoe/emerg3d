from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from blog.models import Post
from django.contrib import messages


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


def get_login_page(request):
    return render(request, 'accounts/login.html')


@login_required
def profile(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    user_posts = Post.objects.filter(author=user) if user.is_moderator else []

    return render(request, 'accounts/profile.html', {
        'user': user,
        'user_posts': user_posts
    })

