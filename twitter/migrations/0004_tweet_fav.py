# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_remove_tweet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='fav',
            field=models.IntegerField(default=0),
        ),
    ]
