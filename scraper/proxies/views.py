from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProxyForm
from .models import Proxy


class ProxyCreateView(CreateView):
    model = Proxy
    form_class = ProxyForm
    template_name = 'proxies/proxy_create.html'

    def get_success_url(self):
        url = super().get_success_url()
        if 'btn_save_and_add_another' in self.request.POST:
            url = reverse_lazy('proxies:proxy_create')
        return url
