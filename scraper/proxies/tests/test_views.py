from http import HTTPStatus

from django.urls import reverse

from ..models import Proxy


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
            'region': 'Buenos Aires',
            'city': 'Moron',
            'uptime': 62.1,
            'response': 94,
            'transfer': 69,
        }
        response = client.post(self.url, data=payload, follow=True)
        assert response.status_code == HTTPStatus.OK
