from django.urls import path
from .views import RegistrationView, CustomTokenObtainPairSerializer, UserAuthViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers


router = routers.DefaultRouter()


users_urls = [
    path('login/', CustomTokenObtainPairSerializer.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('me/', UserAuthViewSet.as_view({'get': 'me'}), name='me'),
]
users_urls += router.urls