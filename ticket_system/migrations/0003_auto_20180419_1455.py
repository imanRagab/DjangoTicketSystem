# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_system', '0002_auto_20180419_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_state',
            new_name='ticket_status',
        ),
    ]
