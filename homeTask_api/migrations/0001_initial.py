# Generated by Django 3.1.7 on 2021-04-05 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(verbose_name='Описание задания')),
                ('deadline', models.DateField(verbose_name='Срок сдачи')),
                ('expired', models.BooleanField(default=False, verbose_name='Просрочен ли')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
            },
        ),
        migrations.CreateModel(
            name='CompletedHomeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_file', models.FileField(upload_to='homeTasks/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сделанное домашнее задание',
                'verbose_name_plural': 'Сделанные домашние задания',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='CheckedHomeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_from_admin', models.TextField(blank=True, default='Нет ответа', null=True, verbose_name='Ответ от админа')),
                ('mark', models.IntegerField(blank=True, default=0, null=True, verbose_name='Отметка')),
                ('completed_home_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homeTask_api.completedhometask', verbose_name='Сделанное дз')),
            ],
            options={
                'verbose_name': 'Проверенное домашнее задание',
                'verbose_name_plural': 'Проверенные домашние задания',
                'ordering': ['completed_home_task__user'],
            },
        ),
    ]
