from django.urls import path
from .views import (PostListView, PostDetailView, 
                   PostCreateView, PostUpdateView, 
                   PostDeleteView, CommentCreateView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('logout/', views.user_logout, name='logout'),
]