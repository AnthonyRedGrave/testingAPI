from django.contrib import admin
from .models import HomeTask, CheckedHomeTask, CompletedHomeTask


class CheckedHomeTaskAdmin(admin.ModelAdmin):
    list_display = ['completed_home_task', 'description_from_admin', 'mark', 'status']


admin.site.register(HomeTask)
admin.site.register(CheckedHomeTask, CheckedHomeTaskAdmin)
admin.site.register(CompletedHomeTask)

