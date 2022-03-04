# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from webapp.proxies.models import Proxy


class ScraperItem(DjangoItem):
    django_model = Proxy
