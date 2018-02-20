# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0003_auto_20171213_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='marriage_date',
            field=models.DateField(null=True, verbose_name=b'Marriage Date', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=True, verbose_name=b'Birth Date', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_date',
            field=models.DateField(null=True, verbose_name=b'Death Date', blank=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(help_text=b'This might be where we could put our OCR generated text??', verbose_name=b'Revised Text', blank=True),
        ),
    ]
