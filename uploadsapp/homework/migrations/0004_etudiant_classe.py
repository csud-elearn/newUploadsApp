# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_auto_20150419_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='classe',
            field=models.ManyToManyField(to='homework.Classe'),
        ),
    ]
