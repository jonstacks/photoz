# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporaryimage',
            name='image',
            field=models.ImageField(upload_to=photos.models.calculate_path),
        ),
    ]
