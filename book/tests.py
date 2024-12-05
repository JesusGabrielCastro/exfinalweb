from django.urls import include, path,reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item

class AccountTests(APITestCase):
   
    def test_create_book_and_retrieve(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('book-list')
        data = {'name': 'Test', 'description': 'Testing', 'price': 50.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Test')

        