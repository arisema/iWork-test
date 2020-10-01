from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets, generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import UserSerializer, ItemSerializer, Item


class UserCreateView(generics.CreateAPIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user_token = Token.objects.create(user=user)
                return Response({'token': user_token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.CreateAPIView):
    def post(self, request, format='json'):
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            user_token = Token.objects.get(user=user)
            return Response({'token': user_token.key}, status=status.HTTP_200_OK)
    
        return Response({'error': "Please make sure the credentials are correct, or try signing-up!"}, status=status.HTTP_400_BAD_REQUEST)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [ permissions.IsAuthenticated ]
    serializer_class = ItemSerializer
