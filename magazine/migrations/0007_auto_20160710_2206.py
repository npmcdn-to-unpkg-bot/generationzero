# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-10 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20160509_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='well_image',
            field=models.CharField(blank=True, help_text="Image to fill this entry's well (higher priority than 'well text').", max_length=200),
        ),
        migrations.AlterField(
            model_name='entry',
            name='well_text',
            field=models.TextField(blank=True, help_text="Text to fill this entry's well (if blank, 'entry content' will be used)."),
        ),
    ]
