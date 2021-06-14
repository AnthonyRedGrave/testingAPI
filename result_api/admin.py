from django.contrib import admin
from .models import Result, UserAnswer, IntermediateResult


class IntermediateResultAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'user', 'is_done']


admin.site.register(Result)
admin.site.register(UserAnswer)
admin.site.register(IntermediateResult, IntermediateResultAdmin)