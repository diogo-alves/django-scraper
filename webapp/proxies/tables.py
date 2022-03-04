import django_tables2 as tables

from .models import Proxy


class ProxyTable(tables.Table):
    ip_address = tables.Column(linkify=True)
    port = tables.Column(linkify=True)
    country = tables.Column(linkify=True)
    city = tables.Column(linkify=True)
    speed = tables.Column(linkify=True)
    protocol = tables.Column(linkify=True, verbose_name='Type')
    anonymity = tables.Column(linkify=True)
    actions = tables.TemplateColumn(
        template_name='proxies/proxy_list_actions.html',
        orderable=False,
    )

    class Meta:
        model = Proxy
        fields = (
            'ip_address',
            'port',
            'country',
            'city',
            'speed',
            'protocol',
            'anonymity',
        )
        per_page = 10
