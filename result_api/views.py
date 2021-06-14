from django.shortcuts import get_object_or_404
from .models import Result, UserAnswer, IntermediateResult
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import ResultSerializer, UserAnswerSerializer, IntermediateResultSerializer
from test_api.models import Test
from rest_framework.response import Response


class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def list(self, request, *args, **kwargs):
        queryset = UserAnswer.objects.filter(user = request.user)
        serializer = UserAnswerSerializer(queryset, many=True)
        return Response(serializer.data)


class UserAnswerRetrieve(ReadOnlyModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def retrieve(self, request, pk=None):
        queryset = UserAnswer.objects.all()
        user_answer = get_object_or_404(queryset, pk=pk)
        serializer = UserAnswerSerializer(user_answer)
        return Response(serializer.data)


class IntermediateResultViewSet(ModelViewSet):
    queryset = IntermediateResult.objects.all()
    serializer_class = IntermediateResultSerializer

    def list(self, request, *args, **kwargs):
        for quiz in Test.objects.all():
            if not IntermediateResult.objects.filter(user = request.user, quiz = quiz).exists():
                IntermediateResult.objects.create(user = request.user, quiz = quiz)
        queryset = IntermediateResult.objects.all()
        serializer = IntermediateResultSerializer(queryset, many=True)
        return Response(serializer.data)
