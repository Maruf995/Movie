from rest_framework import generics, permissions

# Create your views here.
from .models import Movie, Genre
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieListSerializer, GenresListSerializer
from .service import MovieFilter

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = MovieListSerializer
    filterset_class = MovieFilter
    # permission_classes = [permissions.IsAuthenticated]


class GenresListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresListSerializer
    # permission_classes = [permissions.IsAuthenticated]