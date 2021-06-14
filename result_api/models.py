from django.db import models
from django.contrib.auth.models import User
from test_api.models import Test, Question
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Result(models.Model):
    quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField('Набранные балы')
    result_data = models.JSONField('Результат', default=dict)

    def __str__(self):
        return f"{self.quiz} - {self.user} - {self.score}"

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'


# промежуточный результат
class IntermediateResult(models.Model):
    quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField('Сделан', default=False)

    def __str__(self):
        return f"Промежуточный результат: {self.quiz} - {self.user}"


class UserAnswer(models.Model):
    intermediate_result = models.ForeignKey(IntermediateResult, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Ответ', max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text


@receiver(post_save, sender = Test)
def save_test(sender, instance, *args, **kwargs):
    for user in User.objects.all():
        if not IntermediateResult.objects.filter(quiz = instance, user = user):
            print("создаем тест для пользователя", user)
            IntermediateResult.objects.create(quiz = instance, user = user)





