# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-03 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propetyinfo',
            name='profile_picture',
            field=models.FileField(upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='propetyinfo',
            name='property_brochure',
            field=models.FileField(upload_to='brochure'),
        ),
    ]
