from rest_framework import serializers
from smartapp.models import About, Project, Musings

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('description', 'image')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('titel', 'image', 'link', 'github')

class MusingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musings
        fields = ('title', 'image', 'description')
