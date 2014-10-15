# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('msgboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
