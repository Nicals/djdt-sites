from debug_toolbar.toolbar import DebugToolbar
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.test.client import RequestFactory
import pytest

from djdt_sites.panel import SitesPanel


@pytest.mark.django_db
def test_generate_stats():
    site = Site.objects.create(name='site', domain='site.example.org')
    factory = RequestFactory()
    request = factory.get('/')
    request.site = site
    response = HttpResponse(200)
    panel = SitesPanel(DebugToolbar(request))

    panel.generate_stats(request, response)

    assert panel.get_stats() == {
        'current': site,
        'sites': [
            {'is_current': False, 'site': Site.objects.get(pk=1)},  # default site
            {'is_current': True, 'site': site},
        ]}


@pytest.mark.django_db
def test_nav_subtitle():
    site = Site.objects.create(name='site', domain='site.example.org')
    factory = RequestFactory()
    request = factory.get('/')
    request.site = site
    response = HttpResponse(200)
    panel = SitesPanel(DebugToolbar(request))

    panel.generate_stats(request, response)

    assert panel.nav_subtitle == 'site.example.org'
