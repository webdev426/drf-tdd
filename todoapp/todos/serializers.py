from django.contrib.auth.models import User
from rest_framework import serializers
from todos.models import ToDo


class ToDoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class ToDoSerializer(serializers.ModelSerializer):
    user = ToDoUserSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = ("user", "name", "done", "date_created")
