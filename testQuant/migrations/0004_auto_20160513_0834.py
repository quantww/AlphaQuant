# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-13 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testQuant', '0003_auto_20160513_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u6570'),
        ),
    ]
