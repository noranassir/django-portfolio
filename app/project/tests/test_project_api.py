from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Project


class ProjectAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(
            title='Test Project',
            description='This is a test project.',
            source_link='http://example.com',
        )

    def test_list_projects(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Project')
