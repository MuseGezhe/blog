# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-07 13:02
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
