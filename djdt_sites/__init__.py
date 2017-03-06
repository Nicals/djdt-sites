"""This app is designed to add some django.contrib.sites support to
django-debug-toolbar.

A new panel ddt_sites.panel.SitesPanel allows to list all existing sites and
to switch from one to another.

The ddt_sites.middleware.SwitchSiteMiddleware must be registered after
any other sites selection middleware.
"""

from django.conf import settings
from django.contrib.sites.models import Site
from debug_toolbar.panels import Panel


class SitesPanel(Panel):
    title = "Sites"
    has_content = True
    template = 'ddt_sites/panel.html'

    @property
    def nav_subtitle(self):
        try:
            return self.get_stats().get('current').domain
        except AttributeError:
            return ''

    def generate_stats(self, request, response):
        from django.contrib.sites.models import Site
        self.record_stats({
            'current': request.site,
            'sites': [
                {
                    'site': site,
                    'is_current': site == request.site,
                }
                for site in Site.objects.all().order_by('pk')
            ],
        })


def switch_site_middleware(get_response):
    def middleware(request):
        if request.META.get('REMOTE_ADDR', None) in settings.INTERNAL_IPS:
            try:
                request.site = Site.objects.get(pk=request.COOKIES['djdt_site'])
            except KeyError:
                pass

        return get_response(request)

    return middleware
