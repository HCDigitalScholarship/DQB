# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeName', models.CharField(max_length=100, verbose_name=b'Location')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orgName', models.CharField(max_length=100, verbose_name=b'Organization Name')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.TextField(verbose_name=b'Reference')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=100, verbose_name=b'Image File')),
                ('text', models.TextField(verbose_name=b'Revised Text', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='bio_info',
        ),
        migrations.RemoveField(
            model_name='person',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='other_filename',
        ),
        migrations.RemoveField(
            model_name='person',
            name='locations',
        ),
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.IntegerField(serialize=False, verbose_name=b'Person ID', primary_key=True),
        ),
        migrations.RemoveField(
            model_name='person',
            name='references',
        ),
        migrations.AddField(
            model_name='person',
            name='textfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, blank=True, to='dqb_app.Text', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='locations',
            field=models.ManyToManyField(to='dqb_app.Location', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='references',
            field=models.ManyToManyField(to='dqb_app.Reference', blank=True),
        ),
    ]
