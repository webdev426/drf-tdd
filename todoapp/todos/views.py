from rest_framework.generics import ListAPIView
from todos.models import ToDo
from todos.serializers import ToDoSerializer


class TodoListAPIView(ListAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()