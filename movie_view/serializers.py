from rest_framework import serializers

from .models import Movie, Genre


class GenresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField(source='get_genres')
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'title']

    def get_genres(self, obj):
        return GenresListSerializer(obj.genres, many=True).data
