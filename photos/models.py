import uuid
from datetime import timedelta

from django.db import models

# Create your models here.
class TemporaryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    ttl = models.DurationField()
