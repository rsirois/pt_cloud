# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 13:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_auto_20170705_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuite',
            name='date_run',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
