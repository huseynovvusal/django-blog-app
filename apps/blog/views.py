from apps.blog.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import BlogListOutputSerializer, BlogCreateInputSerializer
from .selectors import blog_list
from .services import create_blog, update_blog, delete_blog
from .permissions import IsOwnerOrReadOnly
from .models import Blog
from rest_framework import serializers

from apps.common.pagination import LimitOffsetPagination

class BlogListCreateApi(APIView):
    permission_classes = [IsAuthenticated]
    
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class InputSerializer(serializers.Serializer):
        search = serializers.CharField(required=False)
        author_id = serializers.IntegerField(required=False)
        created_at = serializers.DateField(required=False)

    def get(self, request):
        filters_serializer = self.InputSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        blogs = blog_list(filters=filters_serializer.validated_data)
        
        paginator = self.Pagination()
        paginated_blogs = paginator.paginate_queryset(blogs, request)
        
        serializer = BlogListOutputSerializer(paginated_blogs, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BlogCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        blog = create_blog(
            user=request.user,
            title=serializer.validated_data['title'],
            content=serializer.validated_data['content']
        )

        output_serializer = BlogListOutputSerializer(blog)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

class BlogDetailApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, _request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        serializer = BlogListOutputSerializer(blog)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)

        self.check_object_permissions(request, blog)

        serializer = BlogCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        blog = update_blog(
            blog=blog,
            title=serializer.validated_data['title'],
            content=serializer.validated_data['content']
        )

        output_serializer = BlogListOutputSerializer(blog)

        return Response(output_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)

        self.check_object_permissions(request, blog)

        delete_blog(blog)

        return Response(status=status.HTTP_204_NO_CONTENT)
        