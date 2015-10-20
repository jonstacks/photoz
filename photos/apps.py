from django.apps import AppConfig


class PhotosConfig(AppConfig):
    name = "photos"
    verbose_name = "Photos"

    def ready(self):
        import photos.signals
