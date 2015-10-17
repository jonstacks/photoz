# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20151014_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporaryimage',
            name='ttl',
            field=models.DurationField(default=datetime.timedelta(1), choices=[(datetime.timedelta(1), b'A Day'), (datetime.timedelta(31), b'A Month'), (datetime.timedelta(366), b'A Year')]),
        ),
    ]
