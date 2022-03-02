import pytest

from ..forms import ProxyForm
from ..models import Proxy


@pytest.fixture
def proxy_form():
    return ProxyForm()


class TestProxyForm:
    def test_model_used(self, proxy_form):
        assert proxy_form._meta.model == Proxy

    def test_fields_used(self, proxy_form):
        form_fields = list(proxy_form.base_fields)
        assert form_fields == [
            'ip_address',
            'port',
            'protocol',
            'anonymity',
            'country',
            'region',
            'city',
            'uptime',
            'response',
            'transfer',
        ]

    def test_required_fields(self, proxy_form):
        assert proxy_form.fields['ip_address'].required
        assert proxy_form.fields['port'].required
        assert proxy_form.fields['protocol'].required
        assert proxy_form.fields['country'].required
        assert proxy_form.fields['uptime'].required
        assert proxy_form.fields['response'].required
        assert proxy_form.fields['transfer'].required
