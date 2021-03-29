"""Cart Admin: Details to show in admin page"""

# Python imports
# Django imports
from django.contrib import admin

# 3rd party apps
# Local app imports
from .cart import Cart


'''class Cartadmin(admin.ModelAdmin):
    """View details relating to Category objects"""

    #form = CategoryForm
    model = Cart
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

admin.site.register(Cart, Cartadmin,)'''
