from django.contrib import admin
from .models import *


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'test']
    inlines = [AnswerInLine]


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'difficulty', 'required_score', 'number_questions']


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)



