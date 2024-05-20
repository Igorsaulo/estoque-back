from rest_framework import viewsets, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action


@extend_schema(request=CustomUserSerializer, responses=CustomUserSerializer)
class RegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer


@extend_schema(request=CustomUserSerializer, responses=CustomUserSerializer)
class CustomTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            return super().post(request, *args, **kwargs)
        return Response({"error": "Invalid credentials"}, status=400)

@extend_schema(request=CustomUserSerializer, responses=CustomUserSerializer)
class UserAuthViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)