# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touchpoint', '0003_touchpoint_rule_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touchpoint',
            name='rule_approved',
            field=models.BooleanField(default=None),
        ),
    ]
