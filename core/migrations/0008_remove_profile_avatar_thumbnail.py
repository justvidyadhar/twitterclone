# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180401_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar_thumbnail',
        ),
    ]
