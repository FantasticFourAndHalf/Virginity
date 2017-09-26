# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-26 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virginityapp', '0002_dish_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gift_card_client_by', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gift_card_client_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'dishes'},
        ),
        migrations.RemoveField(
            model_name='giftcard',
            name='by',
        ),
        migrations.RemoveField(
            model_name='giftcard',
            name='description',
        ),
        migrations.RemoveField(
            model_name='giftcard',
            name='to',
        ),
        migrations.AddField(
            model_name='giftcard',
            name='name',
            field=models.CharField(default='Prime', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftcard',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=6),
        ),
        migrations.AddField(
            model_name='gift',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_gift_card', to='virginityapp.GiftCard'),
        ),
    ]
