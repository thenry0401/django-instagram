# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_post_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
