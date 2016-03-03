from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    # url(r'^todos/', include('todos.urls', namespace='todos')),
    url(r'^users/', include('users.urls', namespace='users')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
