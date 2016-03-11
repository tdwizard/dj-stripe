# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djstripe', '0003_accounttransfer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounttransfer',
            name='user',
        ),
        migrations.AddField(
            model_name='accounttransfer',
            name='created_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
