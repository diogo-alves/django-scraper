from django.urls import path

from .views import ProxyCreateView, ProxyListView, ProxyUpdateView

app_name = 'proxies'


urlpatterns = [
    path('', ProxyListView.as_view(), name='proxy_list'),
    path('novo/', ProxyCreateView.as_view(), name='proxy_create'),
    path('<int:pk>/editar/', ProxyUpdateView.as_view(), name='proxy_update'),
]
