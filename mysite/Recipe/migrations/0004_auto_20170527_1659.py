# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0003_auto_20170527_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavoring',
            name='manufacturer',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='flavoring',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
