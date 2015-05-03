# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_etudiant_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devoir',
            name='reponse',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
