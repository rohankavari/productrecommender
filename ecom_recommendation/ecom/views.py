# ecom/views.py

from django.shortcuts import render
from .models import Product, User, Recommendation

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Similar views for users and recommendations
