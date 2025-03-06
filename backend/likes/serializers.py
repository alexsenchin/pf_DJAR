from rest_framework import serializers
from .models import Like
from posts.models import Post
from posts.models import Comment

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True, required=False)
    comment = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        model = Like
        fields = ['user', 'post', 'comment', 'value']
