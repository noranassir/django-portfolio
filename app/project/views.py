from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from core.models import Project
from project import serializers

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})