"""Order Admin: Details to show in admin page"""

# Python imports
# Django imports
from django.contrib import admin

# 3rd party apps
# Local app imports
from .models import Order, OrderItem


class Orderadmin(admin.ModelAdmin):
    """View details relating to Order objects"""

    #form = CategoryForm
    model = Order
    list_display = ('__str__', 'email', 'paid', 'paid_amount')
    list_filter = ('paid',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'email',
                'zipcode',
                'place',
                'paid',
                'paid_amount'
            ),
        }),
    )
    search_fields = ('__str__',)
    ordering = ('paid', 'paid_amount',)


class OrderItemadmin(admin.ModelAdmin):
    """View details relating to Order Item objects"""

    #form = CategoryForm
    model = OrderItem
    list_display = ('__str__', 'price', 'quantity')
    list_filter = ('price',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'order',
                'product',
                'price',
                'quantity',
            ),
        }),
    )
    search_fields = ('product', 'price',)
    ordering = ('__str__',)


admin.site.register(Order, Orderadmin,)
admin.site.register(OrderItem, OrderItemadmin,)
