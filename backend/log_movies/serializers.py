from rest_framework import serializers
from .models import Movie, UserMovieList

class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = "__all__"

class UserMovieListSerializer(serializers.Serializer):
    movie = MovieSerializer()

    class Meta:
        model = UserMovieList
        fields = ['id', 'movie', 'status']