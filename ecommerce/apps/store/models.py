"""Store Models: Contains database classes and functions"""

# Python imports
# Django imports
from django.db import models

# 3rd party apps
# Local app imports


class Category(models.Model):

    """
      Category model
        * Title
        * Slug
      """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):

    """
      Product model
        * Title
        * Slug
        * Description
        * Price
        * category
      """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        'category', related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
