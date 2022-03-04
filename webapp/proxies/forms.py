from django import forms

from .models import Proxy


class ProxyForm(forms.ModelForm):
    class Meta:
        model = Proxy
        fields = (
            'ip_address',
            'port',
            'protocol',
            'anonymity',
            'country',
            'city',
            'speed',
        )
