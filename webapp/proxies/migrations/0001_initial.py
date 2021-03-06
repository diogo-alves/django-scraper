# Generated by Django 4.0.3 on 2022-03-02 20:56

import django.core.validators
from django.db import migrations, models

import webapp.proxies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('ip_address', models.GenericIPAddressField()),
                (
                    'port',
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(65535)
                        ]
                    ),
                ),
                (
                    'protocol',
                    models.CharField(
                        choices=[('http', 'HTTP'), ('https', 'HTTPS')],
                        default='http',
                        max_length=5,
                    ),
                ),
                (
                    'anonymity',
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, 'None'),
                            ('A', 'Anonymous'),
                            ('HA', 'High Anonymous'),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                ('country', models.CharField(max_length=60)),
                (
                    'region',
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    'city',
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ('uptime', models.FloatField()),
                ('response', models.FloatField()),
                ('transfer', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'proxies',
                'db_table': 'proxy',
            },
        ),
    ]
