# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20160118_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='magazine.Issue'),
        ),
    ]