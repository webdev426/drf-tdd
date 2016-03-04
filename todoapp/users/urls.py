from django.conf.urls import url
from users.views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    url(r'^$', UserRegistrationAPIView.as_view()),
    url(r'^login/$', UserLoginAPIView.as_view()),
    url(r'^logout/$', UserLogoutAPIView.as_view()),
]