from django.conf.urls import url
from todos.views import ToDoListCreateAPIView, ToDoDetailAPIView

urlpatterns = [
    url(r'^$', ToDoListCreateAPIView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', ToDoDetailAPIView.as_view(), name="detail"),
]