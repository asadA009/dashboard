from .models import confrence
from django.forms import ModelForm


class confrence(ModelForm):
    class Meta:
        model = confrence
        fields = ['name', 'city', 'venu',
                  'email','number']
