from django.shortcuts import render

# Create your views here.
from .models import Product


def product_view(request):
    return render(request, 'product/detail.html', {})
