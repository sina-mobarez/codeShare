from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, File, CollaborationSession
from editor.serializers import (
    ProjectSerializer,
    FileSerializer,
    CollaborationSessionSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]


class CollaborationSessionViewSet(viewsets.ModelViewSet):
    queryset = CollaborationSession.objects.all()
    serializer_class = CollaborationSessionSerializer
    permission_classes = [IsAuthenticated]
