from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
