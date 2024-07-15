from rest_framework.routers import DefaultRouter
from .api import TaskViewSet

# Crear una instancia del enrutador
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='tasks')

# Definir las URLs
urlpatterns = router.urls
