# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djstripe', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTransfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=7, decimal_places=2)),
                ('currency', models.CharField(max_length=3)),
                ('account', models.ForeignKey(to='djstripe.Account')),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account transfer',
            },
        ),
    ]
