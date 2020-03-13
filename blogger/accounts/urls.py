from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    LoginViewSet,
    UserRegistrationView,
)

router = DefaultRouter()

router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', UserRegistrationView,
                basename='register')

urlpatterns = [
    path('', include(router.urls)),
]
