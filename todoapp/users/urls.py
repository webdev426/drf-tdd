from django.conf.urls import url
from users.views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    url(r'^$', UserRegistrationAPIView.as_view()),
    url(r'^login/$', UserLoginAPIView.as_view()),
]