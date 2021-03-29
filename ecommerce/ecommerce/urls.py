"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Python imports
# Django imports
from django.contrib import admin
from django.urls import path

# 3rd party apps
# Local app imports
from apps.core.views import frontpage, contact, about
from apps.store.views import product_detail, category_detail
from apps.cart.views import cart_detail
from apps.store.api import api_add_to_cart, api_remove_from_cart, api_increment_quantity

urlpatterns = [
    # * Core urls
    path('', frontpage, name='frontpage'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

    # * Cart urls

    path('cart/', cart_detail, name='cart'),

    # * API urls

    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/increment_quantity/', api_increment_quantity,
         name='api_increment_quantity'),
    path('api/remove_from_cart/', api_remove_from_cart,
         name='api_remove_from_cart'),

    # * Store urls
    path('<slug:category_slug>/<slug:slug>/',
         product_detail, name='product_detail'),
    path('<slug:slug>/',
         category_detail, name='category_detail'),

    # * Admin urls
    path('admin/', admin.site.urls),
]
