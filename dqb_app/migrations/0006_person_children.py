# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0005_auto_20171218_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='children',
            field=models.ManyToManyField(related_name='children_rel_+', to='dqb_app.Person', blank=True),
        ),
    ]
