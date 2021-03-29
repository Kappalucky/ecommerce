"""Core Views: Details on what data to show"""

# Python imports
# Django imports
from decimal import Context
from django.shortcuts import render

# 3rd party apps
# Local app imports
from apps.store.models import Product


def frontpage(request):
    '''List all products on frontpage template'''

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')
