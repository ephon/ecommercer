# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_auto_20151119_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
