# Generated by Django 3.1.7 on 2021-03-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0002_auto_20210325_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='number_questions',
            field=models.IntegerField(default=5, verbose_name='Количество вопросов'),
        ),
    ]
