from django.db.models.signals import post_delete
from django.dispatch import receiver

from photos.models import TemporaryImage

@receiver(post_delete, sender=TemporaryImage)
def image_post_delete_handler(sender, **kwargs):
    temp_image = kwargs['instance']
    temp_image.image.delete(save=False)
