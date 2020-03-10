from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'content', 'created_at')
        model = Content
