# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20150418_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='contraste',
        ),
        migrations.RemoveField(
            model_name='image',
            name='luminosite',
        ),
        migrations.RemoveField(
            model_name='image',
            name='saturation',
        ),
    ]
