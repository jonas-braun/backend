# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
