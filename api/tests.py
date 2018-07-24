from django.test import TestCase
from .models import Category
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the Category model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.category_name = "Test"
        self.category = Category(name=self.category_name)

    def test_model_can_create_a_category(self):
        """Test the category model can create a category."""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewCategoryTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data = {'name': 'Test name', 'description': 'Test description'}
        self.response = self.client.post(
            reverse('create'),
            self.category_data,
            format="json")

    def test_api_can_create_a_category(self):
        """Test the api has created a category."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
