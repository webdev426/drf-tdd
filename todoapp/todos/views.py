from rest_framework.generics import ListCreateAPIView
from todos.models import ToDo
from todos.serializers import ToDoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




