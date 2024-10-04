from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()
router.register('projects', views.ProjectViewSet)

app_name = 'project'

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.project_index, name='project_index'),
    path('list/<int:pk>/', views.project_detail, name='project_detail'),
]
