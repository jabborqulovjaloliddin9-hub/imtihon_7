from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CommentViewSet, PostViewSet, LikeToggleAPIView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('categories', CategoryViewSet, basename='categories')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
]