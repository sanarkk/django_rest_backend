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
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=50,
                                          author_name='Author 3')
        self.book_3 = Book.objects.create(name='Test book Author 1', price=45,
                                          author_name='Author 2')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2,
                                           self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerializer([self.book_1,
                                           self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BooksSerializer([self.book_1,
                                           self.book_3,
                                           self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)