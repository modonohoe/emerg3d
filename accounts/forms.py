from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from .models import Post


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "description"]
