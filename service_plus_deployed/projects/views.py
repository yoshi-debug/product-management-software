from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer