from django.db import models
from django.conf import settings
from .constants import COUNTRY_CHOICES
from django.utils import timezone
from django.core.validators import MinValueValidator


def validate_not_in_past(value):
    if value < timezone.now().date():
        raise ValidationError('Suggested completion date cannot be in the past!')

# in future projects the above can be defined in a validators.py file

class EnquiryTicket(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='Your project or item name')
    description = models.TextField(max_length=400, help_text='What do you want printed and what dimensions, colors, finishes etc.')
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IE')
    completion_date = models.DateField(null=True, blank=True, help_text='(optional)', validators=[validate_not_in_past])
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='€ amount (optional)', validators=[MinValueValidator(0)])
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title


