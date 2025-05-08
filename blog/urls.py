from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (  # Добавляем импорт JWT
    TokenObtainPairView,
    TokenRefreshView,
)
from posts.views import RegisterView  # Импорт вашего представления регистрации

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
    # Posts app
    path('', include('posts.urls')),
]