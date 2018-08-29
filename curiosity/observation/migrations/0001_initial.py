# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('uuid', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('data', models.TextField(default='')),
                ('data_type', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]