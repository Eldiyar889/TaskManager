from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.permissons import IsOwner
from projects.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)