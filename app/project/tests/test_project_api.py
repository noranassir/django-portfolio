from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Project

from project.serializers import ProjectSerializer

def create_project(**params):
    defaults = {
        'title': "Test project title",
        'description': 'Test description',
        'source_link': 'www.example.com',
    }

    defaults.update(params)
    project = Project.objects.create(**defaults)
    return project

class ProjectAPITest(TestCase):

    def setUp(self):

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

    def test_project_creation(self):
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.description, 'This is a test description')
        self.assertEqual(self.project.source_link, 'http://example.com')
        self.assertTrue(self.project.image.name.endswith('test_image.jpg'))

    def test_project_string_representation(self):
        self.assertEqual(str(self.project), 'Test Project')
