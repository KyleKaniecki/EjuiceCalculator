# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
