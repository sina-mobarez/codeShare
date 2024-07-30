from rest_framework import serializers
from django.contrib.auth.models import User
from editor.models import Project, File, CollaborationSession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    collaborators = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "visibility", "owner", "collaborators"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "filename", "content", "last_modified", "project"]


class CollaborationSessionSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    active_file = FileSerializer(read_only=True)

    class Meta:
        model = CollaborationSession
        fields = ["id", "project", "active_file", "participants", "session_metadata"]
