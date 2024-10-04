from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Project

from project.serializers import ProjectSerializer


class ProjectAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        self.project = Project.objects.create(
            title='Test Project',
            description='This is a test project.',
            source_link='http://example.com',
            image=self.image
        )

    def test_list_projects(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Project')

    def test_project_image_field(self):
        url = reverse('project-detail', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['image'].endswith('test_image.jpg'))
