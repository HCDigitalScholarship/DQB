# Generated by Django 2.0.1 on 2018-01-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqb_app', '0006_person_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='placeName',
            field=models.CharField(max_length=100, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgName',
            field=models.CharField(max_length=100, verbose_name='Organization Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_date',
            field=models.DateField(blank=True, null=True, verbose_name='Death Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='filename',
            field=models.CharField(blank=True, max_length=100, verbose_name='File Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Person ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='marriage_date',
            field=models.DateField(blank=True, null=True, verbose_name='Marriage Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='ref',
            field=models.TextField(verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='text',
            name='filename',
            field=models.CharField(max_length=100, verbose_name='Image File'),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(blank=True, help_text='This might be where we could put our OCR generated text??', verbose_name='Revised Text'),
        ),
    ]