# Generated by Django 3.1.7 on 2021-04-06 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeTask_api', '0003_completedhometask_home_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometask',
            name='expired',
        ),
    ]