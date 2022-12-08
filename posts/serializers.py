from rest_framework import serializers
from .models import Post
# getting custom user model
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username",)