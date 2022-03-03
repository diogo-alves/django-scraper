from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from .forms import ProxyForm
from .models import Proxy
from .tables import ProxyTable


class ProxyCreateView(CreateView):
    model = Proxy
    form_class = ProxyForm
    template_name = 'proxies/proxy_create.html'
    success_url = reverse_lazy('proxies:proxy_list')

    def get_success_url(self):
        url = super().get_success_url()
        if 'btn_save_and_add_another' in self.request.POST:
            url = reverse_lazy('proxies:proxy_create')
        return url


class ProxyUpdateView(UpdateView):
    model = Proxy
    form_class = ProxyForm
    template_name = 'proxies/proxy_update.html'
    success_url = reverse_lazy('proxies:proxy_list')


class ProxyListView(SingleTableView):
    model = Proxy
    table_class = ProxyTable
    template_name = 'proxies/proxy_list.html'


class ProxyDeleteView(DeleteView):
    model = Proxy
    success_url = reverse_lazy('proxies:proxy_list')
