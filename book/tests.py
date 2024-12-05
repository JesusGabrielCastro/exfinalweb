from django.urls import include, path,reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class AccountTests(APITestCase):
   
    def test_create_book_and_retrieve(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('book-list')
        data = {'title': 'Test', 'author': 'Testing', 'published_date': '2020-01-01', 'isbn': 1234567890}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test')

        