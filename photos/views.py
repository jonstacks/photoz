from django.views.generic import DetailView, ListView

from photos.models import TemporaryImage


class ImageListView(ListView):
    context_object_name = 'images'
    model = TemporaryImage


class ImageDetailView(DetailView):
    context_object_name = 'image'
    model = TemporaryImage
