# Generated by Django 4.1.1 on 2022-09-09 10:30

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localise', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidences',
            options={'verbose_name_plural': ' Incidences'},
        ),
        migrations.AlterField(
            model_name='incidences',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]