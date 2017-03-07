from django.conf import settings
from django.contrib.sites.models import Site


def switch_site_middleware(get_response):
    """Checks the content of a `djdt_site` cookie. If it is present, set
    the current site as being the one with the primary key contained in the
    cookie.
    """
    def middleware(request):
        if request.META.get('REMOTE_ADDR', None) in settings.INTERNAL_IPS:
            try:
                request.site = Site.objects.get(pk=request.COOKIES['djdt_site'])
            except KeyError:
                pass

        return get_response(request)

    return middleware
