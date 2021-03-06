"""Store Views: Details on what data to show"""

# Python imports
# Django imports
from django.shortcuts import get_object_or_404, render

# 3rd party apps
# Local app imports
from .models import Product


def product_detail(request, slug):
    '''List details for a product'''

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)
