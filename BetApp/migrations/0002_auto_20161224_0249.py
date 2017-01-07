# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-23 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='support',
            name='user',
        ),
        migrations.AddField(
            model_name='support',
            name='email',
            field=models.EmailField(default='misachi@outlook.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='support',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]