# Generated by Django 3.1.7 on 2021-04-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_api', '0006_auto_20210404_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result_data',
            field=models.JSONField(default={}, verbose_name='Результат'),
        ),
    ]
