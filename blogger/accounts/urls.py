from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import (
    UserViewSet,
)

from .views import (
    LoginViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
