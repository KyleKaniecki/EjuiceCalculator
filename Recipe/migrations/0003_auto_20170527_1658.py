# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0002_recipe_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
