from django.contrib.auth import logout
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from blog.models import Post
from django.contrib import messages
from ticket.models import EnquiryTicket 


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            custom_user = form.save()
            login(request, custom_user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect(reverse('profile', kwargs={'slug': custom_user.slug}))
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {"form": form})


def get_login_page(request):
    messages.success(request, 'You have successfully logged in.')
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')


@login_required
def profile(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    user_posts = Post.objects.filter(author=user) if user.is_moderator else []

    return render(request, 'accounts/profile.html', {
        'user': user,
        'user_posts': user_posts
    })


@login_required
def profile(request, slug):
    # Get the profile user based on the slug
    profile_user = get_object_or_404(CustomUser, slug=slug)

    # Check if the profile user is the same as the logged-in user
    is_own_profile = profile_user == request.user

    # Fetch the tickets and posts if applicable
    user_tickets = EnquiryTicket.objects.filter(user=profile_user) if is_own_profile else []
    user_posts = Post.objects.filter(author=profile_user) if profile_user.is_moderator else []

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'is_own_profile': is_own_profile,
        'user_tickets': user_tickets,
        'user_posts': user_posts
    })

