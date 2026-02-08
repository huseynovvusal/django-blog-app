from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] 

class BlogListOutputSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  
    
    class Meta:
        model = Blog
        fields = [
            'id', 
            'title', 
            'slug', 
            'content', 
            'author', 
            'created_at', 
            'updated_at'
        ]

class BlogCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()