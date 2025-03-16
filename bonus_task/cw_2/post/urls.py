from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # Главная страница списка постов
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
