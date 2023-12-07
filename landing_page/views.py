from django.shortcuts import render


# Create your views here.


def get_landing_page(request):
    return render(request, 'landing_page/index.html')
