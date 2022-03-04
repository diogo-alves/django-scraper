from http import HTTPStatus

import pytest
from django.urls import reverse

from ..models import Proxy


@pytest.fixture
def proxy(db):
    return Proxy.objects.create(
        ip_address='170.155.5.235',
        port=8080,
        protocol=Proxy.ProtocolType.HTTP,
        anonymity=None,
        country='Argentina',
        city='Moron',
        speed=62,
    )


@pytest.fixture
def proxies(db):
    Proxy.objects.bulk_create(
        [
            Proxy(
                ip_address='170.155.5.235',
                port=8080,
                protocol=Proxy.ProtocolType.HTTP,
                anonymity=None,
                country='Argentina',
                city='Moron',
                speed=62,
            ),
            Proxy(
                ip_address='201.218.146.24',
                port=999,
                protocol=Proxy.ProtocolType.HTTP,
                anonymity=None,
                country='Peru',
                city='Arequipa',
                speed=13,
            ),
        ]
    )


class TestProxyCreateView:
    url = reverse('proxies:proxy_create')

    def test_get_response(self, client):
        response = client.get(self.url)
        assert response.status_code == HTTPStatus.OK

    def test_template_used(self, client):
        response = client.get(self.url)
        assert 'proxies/proxy_create.html' in response.template_name

    def test_create(self, client, db):
        payload = {
            'ip_address': '170.155.5.235',
            'port': 8080,
            'protocol': Proxy.ProtocolType.HTTP,
            'anonymity': '',
            'country': 'Argentina',
            'city': 'Moron',
            'speed': 62,
        }
        response = client.post(self.url, data=payload, follow=True)
        assert response.status_code == HTTPStatus.OK


class TestProxyUpdateView:
    def test_get_response(self, client, proxy):
        url = reverse('proxies:proxy_update', kwargs={'pk': proxy.pk})
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK

    def test_template_used(self, client, proxy):
        url = reverse('proxies:proxy_update', kwargs={'pk': proxy.pk})
        response = client.get(url)
        assert 'proxies/proxy_update.html' in response.template_name

    def test_update(self, client, proxy):
        url = reverse('proxies:proxy_update', kwargs={'pk': proxy.pk})
        speed_value = 90
        payload = {
            'ip_address': '170.155.5.235',
            'port': 8080,
            'protocol': Proxy.ProtocolType.HTTP,
            'anonymity': '',
            'country': 'Argentina',
            'city': 'Moron',
            'speed': speed_value,
        }
        response = client.post(url, data=payload, follow=True)
        proxy_updated = Proxy.objects.get(pk=proxy.pk)
        assert response.status_code == HTTPStatus.OK
        assert proxy_updated.speed == speed_value


class TestProxyListView:
    def test_get_response(self, client, proxies):
        url = reverse('proxies:proxy_list')
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK

    def test_template_used(self, client, proxies):
        url = reverse('proxies:proxy_list')
        response = client.get(url)
        assert 'proxies/proxy_list.html' in response.template_name

    def test_objects_returned(self, client, proxies):
        url = reverse('proxies:proxy_list')
        response = client.get(url)
        object_list = response.context.get('object_list')
        assert len(object_list) == 2


class TestProxDeleteView:
    def test_delete(self, client, proxy):
        url = reverse('proxies:proxy_delete', kwargs={'pk': proxy.pk})
        client.post(url, follow=True)
        assert Proxy.objects.count() == 0

    def test_redirect_after_delete(self, client, proxy):
        url = reverse('proxies:proxy_delete', kwargs={'pk': proxy.pk})
        response = client.post(url)
        assert response['location'] == reverse('proxies:proxy_list')
