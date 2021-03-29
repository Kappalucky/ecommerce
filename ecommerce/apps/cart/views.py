"""Cart Views: Details on what data to show"""

# Python imports
# Django imports
from decimal import Context
from django.shortcuts import render

# 3rd party apps
# Local app imports


def cart(request):
    return render(request, 'cart.html')
