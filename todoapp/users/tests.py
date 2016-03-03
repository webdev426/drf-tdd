import json
from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from users import views


class UserRegistrationAPIViewTestCase(TestCase):
    factory = APIRequestFactory()

    def test_invalid_password(self):
        """
        Test to verify that a post call with invalid passwords
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "password",
            "confirm_password": "INVALID_PASSWORD"
        }
        request = self.factory.post('/api/users/', user_data)
        view = views.UserRegistrationAPIView.as_view()
        response = view(request)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        request = self.factory.post('/api/users/', user_data)
        view = views.UserRegistrationAPIView.as_view()
        response = view(request)
        response.render()
        self.assertEqual(201, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_unique_username_validation(self):
        user_data_1 = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        request = self.factory.post('/api/users/', user_data_1)
        view = views.UserRegistrationAPIView.as_view()
        response = view(request)
        self.assertEqual(201, response.status_code)

        user_data_2 = {
            "username": "testuser",
            "email": "test2@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        request = self.factory.post('/api/users/', user_data_2)
        view = views.UserRegistrationAPIView.as_view()
        response = view(request)
        self.assertEqual(400, response.status_code)
