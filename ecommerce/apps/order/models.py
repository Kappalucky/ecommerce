from django.db import models
from django.contrib.auth import get_user_model

from apps.store.models import Product


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    ARRIVED = 'arrived'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (ARRIVED, 'Arrived'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    place = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    used_coupon = models.CharField(max_length=50, blank=True, null=True)

    payment_intent = models.CharField(max_length=255)

    shipped_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    user = models.ForeignKey(get_user_model(), related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return '%s' % self.first_name

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        'Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return '%s' % self.id
