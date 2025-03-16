from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls')),     # movies/...
    path('articles/', include('blog.urls')),    # articles/...
]
