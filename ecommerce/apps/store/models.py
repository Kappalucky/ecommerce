"""Store Models: Contains database classes and functions"""

# Python imports
from io import BytesIO
# Django imports
from django.db import models
from django.core.files import File

# 3rd party apps
from PIL import Image

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
    image = models.ImageField(
        upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='uploads/', blank=True, null=True)
    category = models.ForeignKey(
        'category', related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
