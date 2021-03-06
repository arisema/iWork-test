from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'first_name', 'last_name', 'password' )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [ 'id', 'name', 'quantity' ]
