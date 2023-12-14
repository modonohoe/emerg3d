from django import forms
from django_summernote.widgets import SummernoteWidget


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }
