from django import forms
from .models import EnquiryTicket
from .constants import COUNTRY_CHOICES
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


class EnquiryTicketForm(forms.ModelForm):
    class Meta:
        model = EnquiryTicket
        fields = ['title', 'description', 'country', 'completion_date', 'budget']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
            'budget': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        }

    def clean_completion_date(self):
        completion_date = self.cleaned_data['completion_date']
        if completion_date < timezone.localdate():
            raise ValidationError("The completion date cannot be in the past.")
        return completion_date

    def __init__(self, *args, **kwargs):
        super(EnquiryTicketForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = COUNTRY_CHOICES
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 8, 'placeholder': 'Enter project description...'})
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'Enter project title...'})
