# Generated by Django 3.1.7 on 2021-04-04 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('result_api', '0005_useranswer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='result_data',
            field=models.JSONField(default='{}', verbose_name='Результат'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
