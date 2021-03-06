# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 16:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('plusVotes', models.IntegerField(default=0)),
                ('minusVotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('categories', models.CharField(max_length=500)),
                ('answered', models.IntegerField(default=0)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='questionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AA.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
