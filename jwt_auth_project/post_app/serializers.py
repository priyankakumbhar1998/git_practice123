from rest_framework import serializers
from . models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'


    def get_owner_username(self,obj):
        return obj.owner.username