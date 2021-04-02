"""Cart Views: Details on what data to show"""

# Python imports
# Django imports
from django.conf import settings
from django.shortcuts import render

# 3rd party apps
# Local app imports
from .cart import Cart


def cart_detail(request):

    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (
            product.id, product.title, product.price, item['quantity'], item['total_price'],)

        productsstring = productsstring + b

    context = {
        'cart': cart,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(',')
    }

    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html')