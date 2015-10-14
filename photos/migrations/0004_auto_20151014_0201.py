# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20151014_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temporaryimage',
            options={'ordering': ['-created_dt']},
        ),
    ]
