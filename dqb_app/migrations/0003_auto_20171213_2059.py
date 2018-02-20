# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0002_auto_20171213_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_id',
            new_name='id',
        ),
    ]
