from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from .models import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    model = User
    permission_classes = [ permissions.AllowAny ]
    serializer_class = UserSerializer


