import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from todos.models import ToDo
from todos.serializers import ToDoSerializer


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
        ToDo.objects.create(user=self.user, name="Clean the car!")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == ToDo.objects.count())


class TodoDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.todo = ToDo.objects.create(user=self.user, name="Call Mom!")
        self.url = reverse("todos:detail", kwargs={"pk": self.todo.pk})
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_todo_object_bundle(self):
        """
        Test to verify todo object bundle
        """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        todo_serializer_data = ToDoSerializer(instance=self.todo).data
        response_data = json.loads(response.content)
        self.assertEqual(todo_serializer_data, response_data)

    def test_todo_object_update_authorization(self):
        """
            Test to verify that put call with different user token
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        response = self.client.put(self.url, {"name", "Hacked by new user"})
        self.assertEqual(401, response.status_code)

    def test_todo_object_update(self):
        response = self.client.put(self.url, {"name": "Call Dad!"}, format='json')
        response_data = json.loads(response.content)
        todo = ToDo.objects.get(id=self.todo.id)
        self.assertEqual(response_data.get("name"), todo.name)
