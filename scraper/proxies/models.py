from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class PercentField(models.FloatField):
    description = "Float com valores entre 0 e 100"
    default_validators = [MinValueValidator(0), MaxValueValidator(100)]


class Proxy(models.Model):
    """
    Model que representa um item da listagem do site
    www.freeproxylists.net
    """

    class ProtocolType(models.TextChoices):
        HTTP = 'http', 'HTTP'
        HTTPS = 'https', 'HTTPS'

    class AnonymityType(models.TextChoices):
        ANONYMOUS = 'A', 'Anonymous'
        HIGH_ANONYMOUS = 'HA', 'High Anonymous'

        __empty__ = 'None'

    ip_address = models.GenericIPAddressField()
    port = models.PositiveIntegerField(
        validators=[MaxValueValidator(65_535)],
    )
    protocol = models.CharField(
        max_length=5,
        choices=ProtocolType.choices,
        default=ProtocolType.HTTP,
    )
    anonymity = models.CharField(
        max_length=2,
        choices=AnonymityType.choices,
        null=True,
        blank=True,
    )
    country = models.CharField(max_length=60)
    region = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    uptime = PercentField()
    response = PercentField()
    transfer = PercentField()

    class Meta:
        db_table = 'proxy'
        verbose_name_plural = 'proxies'

    def __str__(self):
        """Texto que representa o objeto Proxy"""
        address = f'{self.protocol}://{self.ip_address}:{self.port}'
        return f'{address} ({self.country})'

    def get_absolute_url(self):
        return reverse('proxies:proxy_update', kwargs={'pk': self.pk})
