from django.shortcuts import render

# Create your views here.
import jwt
import json
from rest_framework.response import Response
from accounts.models import User
from rest_framework import viewsets, mixins

from .serializers import PasswordSerializer


class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = PasswordSerializer
    def create(self, request, *args, **kwargs):

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
