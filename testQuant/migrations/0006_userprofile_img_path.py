# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-16 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testQuant', '0005_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img_path',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
