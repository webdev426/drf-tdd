from django.conf.urls import url
from users.views import UserRegistrationAPIView, UserAuthenticationAPIView

urlpatterns = [
    url(r'^$', UserRegistrationAPIView.as_view()),
    url(r'^authentication/$', UserAuthenticationAPIView.as_view()),
]