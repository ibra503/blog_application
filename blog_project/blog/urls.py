from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostListCreateView, PostDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),


]
