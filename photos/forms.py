from django.forms import ModelForm
from photos.models import TemporaryImage


class TemporaryImageForm(ModelForm):
    class Meta:
        model = TemporaryImage
        fields = ['image', 'ttl']