from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from todos.models import ToDo
from todos.serializers import ToDoSerializer


class ToDoListCreateAPIView(ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def update(self, request, *args, **kwargs):
        todo = self.get_object()
        if not request.user.id == todo.user.id:
            return Response(status=401)
        return super(ToDoDetailAPIView, self).update(request, *args, **kwargs)




