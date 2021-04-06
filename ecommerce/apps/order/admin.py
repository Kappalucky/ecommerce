"""Order Admin: Details to show in admin page"""

# Python imports
import datetime

# Django imports
from django.urls import reverse
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string

# 3rd party apps
# Local app imports
from .models import Order, OrderItem

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)

order_name.short_description = 'Name'

def admin_order_shipped(modelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        html = render_to_string('order_confirmation.html', {'order': order})
        send_mail('Order confirmation', 'Your order has been sent!', 'noreply@ecommerce.com', ['mail@ecommerce.com', order.email], fail_silently=False, html_message=html)
    return

admin_order_shipped.short_description = 'Set shipped'
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """View details relating to Order objects"""

    list_display = ['id', order_name, 'status', 'created_at']
    list_filter = ['created_at', 'status']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped]

'''
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
'''

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
