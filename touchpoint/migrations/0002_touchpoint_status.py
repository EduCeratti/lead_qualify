# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touchpoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touchpoint',
            name='status',
            field=models.CharField(default=b'IM', max_length=2, choices=[(b'IM', b'Imported'), (b'QL', b'Qualified'), (b'DI', b'Distributed')]),
        ),
    ]
