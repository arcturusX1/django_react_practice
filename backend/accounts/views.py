from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

# RegisterView allows new users to register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Required for CreateAPIView
    serializer_class = UserSerializer  # Uses your custom serializer

