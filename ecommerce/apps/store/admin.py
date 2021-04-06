"""Store Admin: Details to show in admin page"""

# Python imports
# Django imports
from django.contrib import admin

# 3rd party apps
# Local app imports
from .models import Category, Product, ProductImage

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    """View details relating to Category objects"""

    #form = CategoryForm
    model = Category
    list_display = ('__str__', 'title', 'slug', 'ordering')
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'title',
                'slug',
                'ordering'
            ),
        }),
    )
    search_fields = ('title', 'slug',)
    ordering = ('title', 'slug', 'ordering')


class Productadmin(admin.ModelAdmin):
    """View details relating to Product objects"""

    #form = CategoryForm
    model = Category
    list_display = ('__str__', 'slug', 'price', 'category')
    list_filter = ('title', 'price')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'title',
                'slug',
                'description',
                'price',
                'category',
                'is_featured',
                'image',
                'thumbnail'
            ),
        }),
    )
    search_fields = ('title', 'slug', 'price', 'category')
    ordering = ('title', 'slug', 'price')


admin.site.register(Product, Productadmin,)
admin.site.register(ProductImage)
