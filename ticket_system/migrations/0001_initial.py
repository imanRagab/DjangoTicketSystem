# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_title', models.CharField(max_length=255)),
                ('ticket_description', models.TextField()),
                ('ticket_user_email', models.CharField(max_length=255)),
                ('ticket_state', models.IntegerField(default=0, max_length=255, choices=[(0, b'Pending'), (1, b'Resolved')])),
                ('ticket_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
