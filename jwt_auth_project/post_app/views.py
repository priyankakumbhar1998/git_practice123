from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAuthenticatedOrAdminOnly
from .pagination import PostViewSetPagination
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import PostUserRateThrottle


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrAdminOnly, IsAdminUser]
    pagination_class = PostViewSetPagination
    throttle_classes = [ PostUserRateThrottle]