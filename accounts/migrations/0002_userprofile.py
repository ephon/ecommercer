# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('myuser_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True, serialize=False, primary_key=True)),
                ('avatar', models.ImageField(null=True, upload_to='user/avatar/')),
                ('gender', models.CharField(default='男', choices=[('men', '男'), ('women', '女')], max_length=2)),
                ('address', models.CharField(blank=True, null=True, max_length=500)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.myuser',),
        ),
    ]
