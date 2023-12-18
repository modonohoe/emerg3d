from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Product


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Product
        fields = '__all__'
