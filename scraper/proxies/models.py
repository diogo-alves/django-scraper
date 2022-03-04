from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class Proxy(models.Model):
    """
    Model que representa um item da listagem do site
    www.freeproxylists.net
    """

    class ProtocolType(models.TextChoices):
        HTTP = 'HTTP', 'HTTP'
        HTTPS = 'HTTPS', 'HTTPS'
        SOCKS4 = 'SOCKS4', 'SOCKS4'
        SOCKS5 = 'SOCKS5', 'SOCKS5'

    class AnonymityType(models.TextChoices):
        LOW = 'Low', 'Low'
        AVERAGE = 'Average', 'Average'
        HIGH = 'High', 'High'

        __empty__ = 'No'

    ip_address = models.GenericIPAddressField()
    port = models.PositiveIntegerField(
        validators=[MaxValueValidator(65_535)],
    )
    protocol = models.CharField(
        max_length=6,
        choices=ProtocolType.choices,
        default=ProtocolType.HTTP,
    )
    anonymity = models.CharField(
        max_length=7,
        choices=AnonymityType.choices,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    speed = models.PositiveIntegerField(
        help_text='in ms',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'proxy'
        verbose_name_plural = 'proxies'

    def __str__(self):
        """Texto que representa o objeto Proxy"""
        address = f'{self.protocol.lower()}://{self.ip_address}:{self.port}'
        if self.country:
            return f'{address} ({self.country})'
        return address

    def get_absolute_url(self):
        return reverse('proxies:proxy_update', kwargs={'pk': self.pk})
