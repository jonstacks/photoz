"""
Removes expired TemporaryImages

"""

from django.core.management.base import BaseCommand, CommandError

from photos.models import TemporaryImage

class Command(BaseCommand):
    help = 'Removes expired images from storage'

    def handle(self, **options):
        for i in TemporaryImage.objects.all():
            if not i.not_expired():
                self.stdout.write("Deleting %s" % i.image.name)
                i.delete()
