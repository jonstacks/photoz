import os
import uuid
from datetime import timedelta

from django.db import models

def calculate_path(instance, filename):
    return "temp_images/{}{}".format(instance.id, instance.extension)

class TemporaryImage(models.Model):
    class Meta:
        ordering = ['-created_dt']

    DAY = timedelta(days=1)
    MONTH = timedelta(days=31)
    YEAR = timedelta(days=366)

    TTL_CHOICES = (
        (DAY, 'A Day'),
        (MONTH, 'A Month'),
        (YEAR, 'A Year'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=calculate_path)
    ttl = models.DurationField(choices=TTL_CHOICES, default=DAY)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('image-detail', args=[self.id])

    @property
    def extension(self):
        name, ext = os.path.splitext(self.image.name)
        return ext
