# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virginityapp', '0003_auto_20170926_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]