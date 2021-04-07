"""Store Views: Details on what data to show"""

"""These are nothing more than manual api view sets. Recreate the equivalence using rest framework"""

# Python imports
# Django imports
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

# 3rd party apps
# Local app imports
from apps.cart.cart import Cart
from .models import Category, Product

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products
    }

    return render(request, 'search.html', context)

def product_detail(request, category_slug, slug):
    '''List details for a product'''

    product = get_object_or_404(
        Product, slug=slug)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)

    # Pretty much a serializer
    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)

    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    cart = Cart(request)

    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False

    context = {
        'product': product,
        'imagesstring': imagesstring
    }

    return render(request, 'product_detail.html', context)


def category_detail(request, slug):
    '''List details for a category'''

    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)
