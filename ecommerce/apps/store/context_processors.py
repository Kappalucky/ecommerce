"""Store Context Processors: """

# Python imports
# Django imports
# 3rd party apps
# Local app imports
from .models import Category


def menu_categories(request):
    categories = Category.objects.all()

    return {'menu_categories': categories}
