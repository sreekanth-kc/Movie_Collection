from rest_framework import serializers
from user_movie_collection.models import Collections, Movies


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ['id', 'title', 'description']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['genres', 'title', 'description']
