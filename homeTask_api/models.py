from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
import os.path
from django.conf import settings
from enum import Enum


class HomeTaskStatus(Enum):
    DONE = 'Выполнено'
    EVALUATED = 'Оценено'


class HomeTask(models.Model):
    task = models.TextField('Описание задания')
    deadline = models.DateField('Срок сдачи', auto_now=False)

    def __str__(self):
        return f'Задание: {self.task}, Срок сдачи: {self.deadline}'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class CompletedHomeTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    txt_file = models.FileField(upload_to='homeTasks/')
    home_task = models.ForeignKey(HomeTask, on_delete=models.CASCADE, related_name='completed')

    def __str__(self):
        return f"Сделанное домашнее задание от {self.user}"

    def delete(self, *args, **kwargs): # удаление файла из хранилища
        if self.txt_file:
            os.remove(self.txt_file.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Сделанное домашнее задание'
        verbose_name_plural = 'Сделанные домашние задания'
        ordering = ['user']


class CheckedHomeTask(models.Model):
    completed_home_task = models.OneToOneField(CompletedHomeTask, on_delete=models.CASCADE, verbose_name='Сделанное дз')
    description_from_admin = models.TextField('Ответ от админа', blank=True, null=True, default='Нет ответа')
    mark = models.IntegerField('Отметка', default=0, blank=True, null=True)
    status = models.CharField('Статус',
                              choices=[(status.name, status.value) for status in HomeTaskStatus],
                              default=0,
                              max_length=150)




    def __str__(self):
        if self.mark:
            return f'{self.completed_home_task} - Отметка: {self.mark}'
        else:
            return f'{self.completed_home_task} - Отметка: Нет отметки'

    class Meta:
        verbose_name = 'Проверенное домашнее задание'
        verbose_name_plural = 'Проверенные домашние задания'
        ordering = ['completed_home_task__user']
