# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0006_auto_20170528_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavoring',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flavoring', to='Recipe.Recipe'),
        ),
    ]
