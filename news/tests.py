from django.test import TestCase, Client

from .models import *
from .views import *


class LinksTestCases(TestCase):
    def setUp(self) -> None:
        self.link = Links.objects.create(link='https://www.youtube.com/watch?v=Dxk91fSK8WM&ab_channel=PyCoding')

    def test_response_from_lib_view(self):
        client = Client()
        response = client.get('/all/')
        self.assertEqual(response.status_code, 200)
