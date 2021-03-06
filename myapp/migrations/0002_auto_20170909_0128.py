# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.ManyToManyField(related_name='Post', to='myapp.Course'),
        ),
    ]
