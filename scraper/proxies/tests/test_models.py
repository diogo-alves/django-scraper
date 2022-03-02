from ..models import Proxy


class TestProxyModel:
    def test_string_representation(self):
        proxy = Proxy(
            ip_address='170.155.5.235',
            port=8080,
            protocol=Proxy.ProtocolType.HTTP,
            anonymity=None,
            country='Argentina',
            region='Buenos Aires',
            city='Moron',
            uptime=62.1,
            response=94,
            transfer=69,
        )
        assert str(proxy) == 'http://170.155.5.235:8080 (Argentina)'
