# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0007_auto_20170528_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]