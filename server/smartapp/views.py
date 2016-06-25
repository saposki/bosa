from rest_framework import viewsets
from smartapp.models import About, Project, Musings
from smartapp.serializers import AboutSerializer, ProjectSerializer, MusingsSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MusingsViewSet(viewsets.ModelViewSet):
    queryset = Musings.objects.all()
    serializer_class = MusingsSerializer
