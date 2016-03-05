import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from todos.models import ToDo


class TodoListCreateAPIViewTestCase(APITestCase):
    url = reverse("todos:list")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_user_authorization(self):
        """
        Test to verify api authorization work with expected
        """
        self.client.credentials()  # remove http authorization header attribute
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

        self.api_authentication()  # add http authorization header attribute
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_create_todo(self):
        response = self.client.post(self.url, {"name": "Clean the room!"})
        self.assertEqual(201, response.status_code)

    def test_user_todos(self):
        """
        Test to verify user todos list
        """
        ToDo.objects.create(name="Clean the car!", user=self.user)
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == ToDo.objects.count())
