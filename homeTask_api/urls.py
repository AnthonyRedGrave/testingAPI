from rest_framework.routers import SimpleRouter
from .views import HomeTaskViewSet, CompletedHomeTaskViewSet, CheckedHomeTaskViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


router = SimpleRouter()
router.register(r'home_tasks', HomeTaskViewSet)
router.register(r'completed_home_tasks', CompletedHomeTaskViewSet)
router.register(r'checked_home_tasks', CheckedHomeTaskViewSet)


urlpatterns = router.urls