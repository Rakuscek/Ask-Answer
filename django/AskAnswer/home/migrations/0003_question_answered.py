# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170107_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
