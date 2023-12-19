from django.db import models
from django.conf import settings # to import user
from .constants import COUNTRY_CHOICES


class EnquiryTicket(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IE')
    completion_date = models.DateField(null=True, blank=True, help_text='(optional)')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='€ amount (optional)')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title


