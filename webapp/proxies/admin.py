from django.contrib import admin

from .models import Proxy


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    ...
