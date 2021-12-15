from .models import Category


def category_list(request):
    return {'category_list': Category.on_site.all(), 'site': request.site}
