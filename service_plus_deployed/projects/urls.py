from rest_framework.routers import DefaultRouter
from projects import views

app_name = "projects"

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet, basename="project")
urlpatterns = router.urls
