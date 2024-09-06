# Generated by Django 5.0.8 on 2024-09-05 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_admintimeslot_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintimeslot',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='admintimeslot',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
