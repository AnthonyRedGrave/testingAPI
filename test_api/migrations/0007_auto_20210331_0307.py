# Generated by Django 3.1.7 on 2021-03-31 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0006_auto_20210330_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['test'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
