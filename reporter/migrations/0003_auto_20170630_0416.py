# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20170630_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='test_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
