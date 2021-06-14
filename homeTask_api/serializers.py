from rest_framework import serializers
from .models import CompletedHomeTask, HomeTask, CheckedHomeTask
import os.path
from django.conf import settings


class HomeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTask
        fields = '__all__'


class CompletedHomeTaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    task = serializers.CharField(source='home_task', read_only = True)

    class Meta:
        model = CompletedHomeTask
        fields = ['id', 'txt_file', 'user', 'home_task', 'task']
        read_only_fields = ('user', )

    def validate(self, data):
        user = self.context['request'].user
        if CompletedHomeTask.objects.filter(user = user,
                                            home_task=data['home_task']):
            raise serializers.ValidationError({"home_task": "Вы уже сделали это задание!"})
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        # создание сделанного задания
        completed_home_task = CompletedHomeTask.objects.create(user=user,
                                                               txt_file=validated_data['txt_file'],
                                                               home_task=validated_data['home_task'])

        # создание проверенного задания со статусом выполнено
        checked_home_task = CheckedHomeTask.objects.create(completed_home_task = completed_home_task,
                                                           status = 'DONE')

        return completed_home_task


class CheckedHomeTaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    completed_task = serializers.CharField(source='completed_home_task', read_only = True)

    class Meta:
        model = CheckedHomeTask
        fields = ['id', 'status', 'description_from_admin', 'mark', 'completed_task']
