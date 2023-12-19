from django import forms
from .models import EnquiryTicket

class EnquiryTicketForm(forms.ModelForm):
    class Meta:
        model = EnquiryTicket
        fields = ['title', 'description', 'country', 'completion_date', 'budget']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
            'budget': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(EnquiryTicketForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = COUNTRY_CHOICES
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 8})
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'Enter title'})
