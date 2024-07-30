from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    visibility = models.CharField(
        max_length=50, choices=[("public", "Public"), ("private", "Private")]
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    collaborators = models.ManyToManyField(
        User, related_name="collaborating_projects", blank=True
    )

    def __str__(self):
        return self.name


class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="files")
    filename = models.CharField(max_length=255)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename


class CollaborationSession(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="sessions"
    )
    active_file = models.ForeignKey(
        File, on_delete=models.SET_NULL, null=True, related_name="active_sessions"
    )
    participants = models.ManyToManyField(User, related_name="sessions")
    session_metadata = models.JSONField(blank=True, null=True)
