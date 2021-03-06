# Generated by Django 3.1.7 on 2021-03-29 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0003_test_number_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NewAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=150)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_api.category')),
                ('question', models.ManyToManyField(blank=True, to='test_api.Question')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.CreateModel(
            name='NewQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=150)),
                ('answer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='test_api.newanswer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='test_api.category')),
                ('choices', models.ManyToManyField(related_name='choices', to='test_api.NewAnswer')),
            ],
        ),
    ]
