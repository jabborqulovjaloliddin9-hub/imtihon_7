from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post, Like, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    category_detail = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image', 'author', 'category', 'likes_count', 'comments_count',
            'created_at', 'updated_at', 'category_detail'
        ]

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Post sarlavhasi 5 ta belgidan kam bo'lmasligi kerak.")
        return value

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]

    def validate(self, attrs):
        request = self.context.get("request")
        user = request.user
        post = attrs.get("post")

        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("siz ushbu postga allaqachon like bosgansiz")
        return attrs
