from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogListOutputSerializer, BlogCreateInputSerializer
from .selectors import blog_list
from .services import create_blog

class BlogListCreateApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, _request):
        blogs = blog_list()
        serializer = BlogListOutputSerializer(blogs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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