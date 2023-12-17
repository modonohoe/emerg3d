from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_moderator = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)
