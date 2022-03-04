from ..models import Proxy


class TestProxyModel:
    def test_string_representation_when_country_was_set(self):
        proxy = Proxy(
            ip_address='170.155.5.235',
            port=8080,
            protocol=Proxy.ProtocolType.HTTP,
            anonymity=None,
            country='Argentina',
            city='Moron',
            speed=62,
        )
        assert str(proxy) == 'http://170.155.5.235:8080 (Argentina)'

    def test_string_representation_when_country_was_not_set(self):
        proxy = Proxy(
            ip_address='170.155.5.235',
            port=8080,
            protocol=Proxy.ProtocolType.HTTP,
            anonymity=None,
            city='Moron',
            speed=62,
        )
        assert str(proxy) == 'http://170.155.5.235:8080'
