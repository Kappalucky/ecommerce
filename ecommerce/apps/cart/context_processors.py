"""Cart Context Processors: """

# Python imports
# Django imports
# 3rd party apps
# Local app imports
from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
