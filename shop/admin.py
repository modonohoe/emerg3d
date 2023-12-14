from django.contrib import admin
from .models import Product
from .forms import ProductAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'category')
