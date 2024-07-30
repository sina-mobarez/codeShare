from django.contrib import admin
from editor.models import Project, File, CollaborationSession

# Register your models here.

admin.site.register(File)
admin.site.register(Project)
admin.site.register(CollaborationSession)
