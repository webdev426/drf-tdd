from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        return Response("ok")
        return super(UserRegistration, self).create(request, *args, **kwargs)
