import uuid

from django.db import models

def calculate_path(instance, filename):
    return "temp_images/{}".format(instance.id)

class TemporaryImage(models.Model):
    class Meta:
        ordering = ['-created_dt']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=calculate_path)
    ttl = models.DurationField()
