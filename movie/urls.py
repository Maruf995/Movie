from django.contrib import admin
from django.urls import path, include
from movie_view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', views.MovieListView.as_view()),
    path('api/v1/genres/', views.GenresListView.as_view()),
    path('auth/', include('djoser.urls')),
    path('api/v1/user/', include('user.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]