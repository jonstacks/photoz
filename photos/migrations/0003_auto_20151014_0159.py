# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20151014_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temporaryimage',
            old_name='created_at',
            new_name='created_dt',
        ),
        migrations.RenameField(
            model_name='temporaryimage',
            old_name='updated_at',
            new_name='updated_dt',
        ),
    ]
