from django.shortcuts import render

# Create your views here.
import jwt
import json
from rest_framework.response import Response
from accounts.models import User
from rest_framework import viewsets, mixins, status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login


from .serializers import PasswordSerializer


class UserRegistrationView(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = PasswordSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data['username']

        user = User.objects.filter(username=username).first()
        if user:
            response = {"username exist"}
            return Response(response)

        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response)


class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = PasswordSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not request.data:
            return Response({"Error"})

        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=username, password=password)

        except User.DoesNotExist:
            return Response({'Error user not exist'})

        if user:
            payload = {

                'id': user.id,
                'username': user.username
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            rep = {**payload, **jwt_token}

            return Response(
                rep,
                status=200,
                content_type="application/json"

            )
        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=400,
                content_type="application/json"
            )
