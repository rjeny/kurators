# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurator_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curator',
            name='phone',
            field=models.CharField(default='000', max_length=12, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curtime',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='curtime',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
    ]