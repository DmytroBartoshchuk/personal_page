from .models import CustomLink


def add_links_to_context(request):
    links = {
        'youtube': CustomLink.objects.get(name='youtube').link,
        'facebook': CustomLink.objects.get(name='facebook').link,
        'instagram': CustomLink.objects.get(name='instagram').link,
        'github': CustomLink.objects.get(name='github').link,
    }
    return {
        'links': links
    }
