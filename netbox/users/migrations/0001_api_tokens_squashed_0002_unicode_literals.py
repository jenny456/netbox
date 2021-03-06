# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 17:43
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('users', '0001_api_tokens'), ('users', '0002_unicode_literals')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=40, unique=True, validators=[django.core.validators.MinLengthValidator(40)])),
                ('write_enabled', models.BooleanField(default=True, help_text='Permit create/update/delete operations using this key')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': [],
            },
        ),
    ]
