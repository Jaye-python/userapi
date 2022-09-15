from django.test import TestCase
from rest_framework.test import APITestCase


class UserAPITestCase(APITestCase):

    def test_create_new_user_succeeds(self):
        url = '/users/'
        data = {
            "first_name": "john",
            "last_name": "smith"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_endpoint_succeeds(self):
        url = '/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)