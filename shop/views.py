from django.shortcuts import render
from .models import Product


def shop(request):
    products = Product.objects.all()

    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)

    sort_by = request.GET.get('sort_by')
    if sort_by:
        products = products.order_by(sort_by)

    return render(request, 'shop/shop.html', {'products': products})
