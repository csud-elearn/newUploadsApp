# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nom', models.CharField(max_length=50)),
                ('branche', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titre', models.CharField(max_length=50)),
                ('consigne', models.CharField(max_length=300)),
                ('consigneImg', models.ImageField(null=True, upload_to='professeur/consignes')),
                ('reponse', models.CharField(max_length=300)),
                ('reponseImg', models.ImageField(null=True, upload_to='professeur/corriges')),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('dateReddition', models.DateField()),
                ('classe', models.ManyToManyField(to='homework.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('theme', models.CharField(max_length=1, default='a')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('photo', models.ImageField(upload_to='etudiants/images')),
                ('description', models.CharField(max_length=300, null=True)),
                ('saturation', models.DecimalField(decimal_places=1, max_digits=2)),
                ('contraste', models.DecimalField(decimal_places=1, max_digits=2)),
                ('luminosite', models.DecimalField(decimal_places=1, max_digits=2)),
                ('date', models.DateField(auto_now_add=True)),
                ('devoir', models.ForeignKey(to='homework.Devoir')),
                ('etudiant', models.ForeignKey(to='homework.Etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('theme', models.CharField(max_length=1, default='a')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='devoir',
            name='professeur',
            field=models.ForeignKey(to='homework.Professeur'),
        ),
        migrations.AddField(
            model_name='classe',
            name='professeur',
            field=models.ForeignKey(to='homework.Professeur'),
        ),
    ]
