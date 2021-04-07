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

admin.site.register(Product)
admin.site.register(ProductImage)
