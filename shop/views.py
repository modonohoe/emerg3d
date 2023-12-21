from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category


def shop(request):
    products = Product.objects.all()
    categorys = Category.objects.all()

    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)

    sort_by = request.GET.get('sort_by')
    if sort_by:
        products = products.order_by(sort_by)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/shop.html', {'products': products, 'categorys': categorys})
