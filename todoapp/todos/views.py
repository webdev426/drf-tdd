from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todos.models import ToDo
from todos.permissions import IsOwnerTodo
from todos.serializers import ToDoSerializer


class ToDoListCreateAPIView(ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerTodo)
