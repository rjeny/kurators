# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurator_base', '0002_auto_20170826_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='prefix',
        ),
        migrations.AddField(
            model_name='group',
            name='faculty',
            field=models.TextField(choices=[('ФФ', 'ФФ'), ('ХТА', 'ХТА'), ('БТ', 'БТ'), ('ХТП', 'ХТП')], default='ФФ', max_length=7, verbose_name='Факультет'),
            preserve_default=False,
        ),
    ]
