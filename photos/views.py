from django.views.generic import DetailView, ListView

from photos.models import TemporaryImage


class ImagesListView(ListView):
    model = TemporaryImage


class ImageDetailView(DetailView):
    model = TemporaryImage
