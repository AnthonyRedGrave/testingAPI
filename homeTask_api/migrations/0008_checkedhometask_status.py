# Generated by Django 3.1.7 on 2021-04-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeTask_api', '0007_auto_20210407_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkedhometask',
            name='status',
            field=models.CharField(default=0, max_length=150, verbose_name='Статус'),
            preserve_default=False,
        ),
    ]