# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touchpoint', '0004_auto_20180626_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touchpoint',
            name='rule_approved',
            field=models.CharField(default=0, max_length=1, choices=[(0, b'Not available'), (1, b'Approved'), (2, b'Reproved')]),
        ),
    ]
