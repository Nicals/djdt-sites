from django.contrib.sites.models import Site
from django.test.client import RequestFactory
import pytest

from djdt_sites.middleware import switch_site_middleware


def get_response(request):
    return request


@pytest.mark.django_db
def test_set_switch_to_site():
    site = Site.objects.create(name='site', domain='site.example.org')
    factory = RequestFactory()
    request = factory.get('/', REMOTE_ADDR='127.0.0.1')
    request.COOKIES['djdt_site'] = site.pk

    middleware = switch_site_middleware(get_response)
    middleware(request)

    assert request.site == site


@pytest.mark.django_db
def test_skipped_if_not_in_INTERNAL_IPS():
    factory = RequestFactory()
    request = factory.get('/', REMOTE_ADDR='127.0.0.2')

    middleware = switch_site_middleware(get_response)
    middleware(request)

    assert hasattr(request, 'site') is False
