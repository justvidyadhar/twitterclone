# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 11:09
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180401_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='/', upload_to='avatars'),
            preserve_default=False,
        ),
    ]
