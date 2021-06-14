from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class TestTopic(Enum):
    IT = 'IT'
    BUSINESS = 'Business'
    SCHOOL = 'SCHOOL'


class TestDifficulty(Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class Test(models.Model):
    name = models.CharField('Название', max_length=150)
    topic = models.CharField(choices=[(topic.name, topic.value) for topic in TestTopic], max_length=150)
    required_score = models.IntegerField('Нужное количество баллов')
    difficulty = models.CharField('Сложность теста', max_length=100, default=1,
                                  choices=[(difficulty.name, difficulty.value) for difficulty in TestDifficulty])
    number_questions = models.IntegerField('Количество вопросов', default=5)

    def __str__(self):
        return f'{self.name} - {self.difficulty}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    text = models.CharField('Вопрос', max_length=150)
    test = models.ForeignKey(Test, verbose_name='Тест', on_delete=models.CASCADE, related_name='questions')
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.test}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['test', 'created']


class Answer(models.Model):
    text = models.CharField('Текст ответа', max_length=200)
    correct = models.BooleanField('Правильность ответа', default=False)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE, related_name='answers')
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"Вопрос: {self.question.text}, Ответ: {self.text}, Правильнен ли: {self.correct}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


