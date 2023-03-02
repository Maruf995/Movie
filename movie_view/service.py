from django_filters import rest_framework as filters
from movie_view.models import Movie

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class MovieFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres__title', lookup_expr='in')
    tag = filters.CharFilter()
    name = filters.CharFilter
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ['title','tag','genres', 'year']

        