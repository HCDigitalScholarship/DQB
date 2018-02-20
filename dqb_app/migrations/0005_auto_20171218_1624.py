# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0004_auto_20171215_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='textfile',
        ),
        migrations.AddField(
            model_name='person',
            name='filename',
            field=models.CharField(max_length=100, verbose_name=b'File Name', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='text',
            field=models.TextField(null=True, verbose_name=b'Text', blank=True),
        ),
    ]
