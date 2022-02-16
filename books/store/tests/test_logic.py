from django.test import TestCase
from store.logic import operations
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

django.setup()


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(7, 98, '+')
        self.assertEqual(105, result)

    def test_minus(self):
        result = operations(6, 4, '-')
        self.assertEqual(2, result)

    def test_multiply(self):
        result = operations(4, 4, '*')
        self.assertEqual(16, result)