from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post_app.views import PostViewSet
from auth_app.views import UserViewSet
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/access/', token_obtain_pair),
    path('v1/refresh/', token_refresh),
]
