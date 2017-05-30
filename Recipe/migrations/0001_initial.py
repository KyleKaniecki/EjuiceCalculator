# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flavoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('percentage', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('percentage', models.PositiveIntegerField()),
                ('targetAmount', models.PositiveIntegerField()),
                ('targetNicotine', models.PositiveIntegerField()),
                ('vgRatio', models.PositiveIntegerField()),
                ('pgRatio', models.PositiveIntegerField()),
                ('daysToSteep', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='flavoring',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipe.Recipe'),
        ),
    ]