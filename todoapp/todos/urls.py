from django.conf.urls import url
from todos.views import TodoListCreateAPIView

urlpatterns = [
    url(r'^$', TodoListCreateAPIView.as_view(), name="list"),
]