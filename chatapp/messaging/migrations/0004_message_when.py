# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 08:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20170628_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='when',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 6, 28, 8, 6, 35, 233464, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
