# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurator_base', '0003_auto_20170826_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curator',
            old_name='second_name',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='group',
            name='faculty',
            field=models.CharField(choices=[('ФФ', 'ФФ'), ('ХТА', 'ХТА'), ('БТ', 'БТ'), ('ХТП', 'ХТП')], max_length=7, verbose_name='Факультет'),
        ),
    ]
