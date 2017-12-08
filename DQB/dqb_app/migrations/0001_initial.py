# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_id', models.CharField(max_length=50, verbose_name=b'Person ID')),
                ('filename', models.CharField(max_length=100, verbose_name=b'File Name')),
                ('other_filename', models.CharField(max_length=100, verbose_name=b'Associated File', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Last Name', blank=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First Name', blank=True)),
                ('birth_date', models.CharField(max_length=20, verbose_name=b'Birth Date', blank=True)),
                ('death_date', models.CharField(max_length=20, verbose_name=b'Death Date', blank=True)),
                ('locations', models.TextField(verbose_name=b'Locations', blank=True)),
                ('bio_info', models.TextField(verbose_name=b'Biographical Information', blank=True)),
                ('references', models.TextField(verbose_name=b'References', blank=True)),
            ],
        ),
    ]
