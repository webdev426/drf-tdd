from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.permissions import IsOwnerTodo
from todos.serializers import TodoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerTodo)

