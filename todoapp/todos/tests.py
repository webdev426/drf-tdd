from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class ToDoListAPIViewTestCase(APITestCase):
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
