"""Cart Views: Details on what data to show"""

# Python imports
# Django imports
from django.shortcuts import render

# 3rd party apps
# Local app imports
from .cart import Cart


def cart_detail(request):

    cart = Cart(request)
    print(cart)

    context = {
        'cart': cart
    }

    return render(request, 'cart.html', context)
