# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=128)),
                ('address2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('zipcode', models.IntegerField(default=0)),
                ('state', models.CharField(max_length=2)),
                ('dateCreated', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(to='frontend.Profile'),
        ),
    ]
