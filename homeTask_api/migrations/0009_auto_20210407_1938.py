# Generated by Django 3.1.7 on 2021-04-07 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeTask_api', '0008_checkedhometask_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkedhometask',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='checkedhometask',
            name='is_evaluated',
        ),
        migrations.RemoveField(
            model_name='checkedhometask',
            name='status',
        ),
    ]
