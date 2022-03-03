from django.urls import path

from .views import ProxyCreateView

app_name = 'proxies'


urlpatterns = [
    path('novo/', ProxyCreateView.as_view(), name='proxy_create'),
]
