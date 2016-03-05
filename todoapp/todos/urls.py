from django.conf.urls import url
from todos.views import TodoListAPIView

urlpatterns = [
    url(r'^$', TodoListAPIView.as_view(), name="list"),
]