from rest_framework import serializers
from django.contrib.auth import get_user_model
from post_app.serializers import PostSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields =('id', 'username', 'password', 'email', 'posts')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)