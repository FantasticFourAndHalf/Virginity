# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-23 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virginityapp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='multiplicity',
            field=models.IntegerField(default=1),
        ),
    ]