# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(max_length=1000),
        ),
    ]
