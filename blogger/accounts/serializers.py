from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username')
        model = User


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'password')
        model = User
