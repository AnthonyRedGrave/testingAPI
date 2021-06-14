from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import HomeTask, CheckedHomeTask, CompletedHomeTask
from .serializers import HomeTaskSerializer, CompletedHomeTaskSerializer, CheckedHomeTaskSerializer


class HomeTaskViewSet(ReadOnlyModelViewSet):
    queryset = HomeTask.objects.all()
    serializer_class = HomeTaskSerializer


class CompletedHomeTaskViewSet(ModelViewSet):
    queryset = CompletedHomeTask.objects.all()
    serializer_class = CompletedHomeTaskSerializer


class CheckedHomeTaskViewSet(ReadOnlyModelViewSet):
    queryset = CheckedHomeTask.objects.all()
    serializer_class = CheckedHomeTaskSerializer

    def get_queryset(self):
        params = self.request.query_params
        status = params.get('status', None)
        user = self.request.user
        queryset = CheckedHomeTask.objects.filter(completed_home_task__user = user)
        # если фильтруется по статусу
        if status:
            queryset = queryset.filter(status = status)
        return queryset