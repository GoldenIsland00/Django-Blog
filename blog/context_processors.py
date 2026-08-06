from django.conf import settings
from .models import Category, Tag


def site_settings(request):
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'Blog'),
        'SITE_NAME_EN': getattr(settings, 'SITE_NAME_EN', 'Blog'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', ''),
        'categories': Category.objects.all()[:10],
        'popular_tags': Tag.objects.all()[:15],
    }
