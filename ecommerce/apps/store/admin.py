"""Store Admin: Details to show in admin page"""

# Python imports
# Django imports
from django.contrib import admin

# 3rd party apps
# Local app imports
from .models import Category, Product

class Categoryadmin(admin.ModelAdmin):
    """View details relating to Category objects"""

    #form = CategoryForm
    model = Category
    list_display = ('__str__', 'title', 'slug',)
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'title',
                'slug',
            ),
        }),
    )
    search_fields = ('title', 'slug',)
    ordering = ('title', 'slug')

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
                'category'
            ),
        }),
    )
    search_fields = ('title', 'slug', 'price', 'category')
    ordering = ('title', 'slug', 'price')

admin.site.register(Category, Categoryadmin,)
admin.site.register(Product, Productadmin,)