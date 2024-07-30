from rest_framework.routers import DefaultRouter
from editor.views import ProjectViewSet, FileViewSet, CollaborationSessionViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"files", FileViewSet)
router.register(r"sessions", CollaborationSessionViewSet)

urlpatterns = router.urls
