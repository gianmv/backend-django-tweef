from django.db.models.base import Model
from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    # image = serializers.ImageField()
    created_data = serializers.DateTimeField()
    birthday = serializers.DateTimeField()
