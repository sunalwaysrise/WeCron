# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-07-26 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eosram', '0007_profile_eos_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ref',
            field=models.CharField(max_length=64, null=True, verbose_name='\u9080\u8bf7\u8005'),
        ),
    ]
