from rest_framework.routers import SimpleRouter
from .views import ResultViewSet, UserAnswerViewSet, UserAnswerRetrieve, IntermediateResultViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


router = SimpleRouter()
router.register(r'results', ResultViewSet)
router.register(r'user_answers', UserAnswerViewSet)
router.register(r'intermediate_result', IntermediateResultViewSet)

urlpatterns = format_suffix_patterns([
    path('user_answers/<int:pk>/', UserAnswerRetrieve.as_view({'get': 'retrieve'})),
])

urlpatterns += router.urls