from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
	//git practice code added by monika
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names=['post', 'get']