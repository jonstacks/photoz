from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from photos.models import TemporaryImage


class ImageCreateView(CreateView):
    model = TemporaryImage
    fields = ['image', 'ttl']
    template_name_suffix = '_create_form'


class ImageListView(ListView):
    context_object_name = 'images'
    model = TemporaryImage


class ImageDetailView(DetailView):
    context_object_name = 'image'
    model = TemporaryImage
