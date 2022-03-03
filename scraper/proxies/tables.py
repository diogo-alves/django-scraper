import django_tables2 as tables

from .models import Proxy


class ProxyTable(tables.Table):
    ip_address = tables.Column(linkify=True)
    port = tables.Column(linkify=True)
    protocol = tables.Column(linkify=True)
    anonymity = tables.Column(linkify=True)
    country = tables.Column(linkify=True)
    region = tables.Column(linkify=True)
    city = tables.Column(linkify=True)
    uptime = tables.Column(linkify=True)
    response = tables.Column(linkify=True)
    transfer = tables.Column(linkify=True)
    actions = tables.TemplateColumn(
        template_name='proxies/proxy_list_actions.html',
        orderable=False,
    )

    class Meta:
        model = Proxy
        fields = (
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
        )
