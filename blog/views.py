from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Post, Comment, Like
from .serializer import CategorySerializer, PostSerializer, LikeSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Post.objects.select_related('author', 'category').annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True),
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.select_related('user', 'post').all()
        post_id = self.request.query_params.get('post_id')

        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeToggleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        like_filter = Like.objects.filter(user=request.user, post=post)

        if like_filter.exists():
            return Response({"error": "Siz ushbu postga allaqachon like bosgansiz"}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(user=request.user, post=post)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        like_filter = Like.objects.filter(user=request.user, post=post)
        if like_filter.exists():
            like_filter.delete()
            return Response({"message": "Like olib tashlandi"}, status=status.HTTP_200_OK)

        return Response({"error": "Siz bu postga like bosmagansiz"}, status=status.HTTP_400_BAD_REQUEST)
