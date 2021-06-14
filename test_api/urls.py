from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TestViewSet, QuestionViewSet, AnswerViewSet


router = SimpleRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = router.urls