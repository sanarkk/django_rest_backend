from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import os
from store.serializers import BooksSerializer

import django

from store.models import Book

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

django.setup()


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=25)
        book_2 = Book.objects.create(name='Test book 2', price=50)
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
