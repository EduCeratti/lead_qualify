# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touchpoint', '0007_auto_20180627_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='touchpoint',
            name='create_date',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
