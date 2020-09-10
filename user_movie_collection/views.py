import json
from rest_framework.response import Response
from rest_framework.views import APIView
from utilities.mixins import HttpResponseMixin
from utilities.utils import count_frequency, retry_http_request
from rest_framework.permissions import IsAuthenticated
from Movie_Listing.settings import CREDY_MOVIE_API_URL
from user_movie_collection.models import Collections, Movies
from user_movie_collection.serializers import CollectionSerializer, MovieSerializer


class GetMovies(APIView, HttpResponseMixin):
    """
    Class name: GetMovies

    Description: Get movie collection from third party API
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Function Name: get

        Description: Get Movies

        Params: Nil

        Return: list of movies

        """
        page = request.GET.get('page')
        if not page:
            page = 1
        credy_movie_api_url = f'{CREDY_MOVIE_API_URL}{page}'
        try:
            max_tries = 5
            response = retry_http_request(max_tries, credy_movie_api_url)
            if response.status_code == 200:
                return Response(json.loads(response.text))
            else:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=json.loads(response.text))
        except Exception as e:

            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))


class MovieCollection(HttpResponseMixin, APIView):
    """
    Class name: MovieCollection

    Description: Manage users movie collection.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, collection_id=None):
        """
        Function Name: get

        Description: Get user movie collection

        Params: Nil

        Return: list of user movie collection

        """
        try:
            user = request.user
            if collection_id:
                try:
                    collection = Collections.objects.get(user=user, id=collection_id)
                except Collections.DoesNotExist as e:
                    return self.error_response(code='HTTP_204_NO_CONTENT', message='No data')
                try:
                    movies = Movies.objects.filter(collection=collection)
                except Movies.DoesNotExist as e:
                    movies = []
                serializer = MovieSerializer(data=movies, many=True)
                if serializer.is_valid():
                    pass
                response = serializer.data
                response_data = {"title": collection.title,
                                 "description": collection.description,
                                 "movies": response}
                return Response(response_data)
            else:
                collections = Collections.objects.filter(user=user)
                genres_list = []
                for collection in collections:
                    movies = Movies.objects.filter(collection=collection.id)
                    for movie in movies:
                        if movie.genres:
                            genres = movie.genres.replace(' ', '')
                            genres = genres.split(',')
                            genres_list.extend(genres)
                favourite_genres = count_frequency(genres_list)
                serializer = CollectionSerializer(data=collections, many=True)
                if serializer.is_valid():
                    pass
                response = serializer.data

                response_data = {'is_success': True,
                                 'data': {
                                     'collection': response
                                 }, 'favourite_genres': favourite_genres}
                return Response(response_data)
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))

    def post(self, request):
        """
        Function Name: post

        Description: post movies to collection

        Params: Nil

        Return: list of user movie collection

        """
        try:
            user = request.user
            title = request.data.get('title')
            description = request.data.get('description')
            movies = request.data.get('movies')
            saved_collection = Collections.objects.create(user=user, title=title, description=description)
            for movie in movies:
                serializer = MovieSerializer(data=movie)
                if not serializer.is_valid():
                    return self.error_response(code='HTTP_400_BAD_REQUEST', message=serializer.errors)
                Movies.objects.create(title=movie['title'], description=movie['description'],
                                      genres=movie['genres'],
                                      collection=saved_collection)

            return Response({'collection_uuid': saved_collection.id})
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))

    def put(self, request, collection_id=None):
        """
        Function Name: put

        Description: update movies to collection

        Params: title, description, movies

        Return: Updated json

        """
        try:
            user = request.user
            try:
                collection = Collections.objects.get(id=collection_id, user=user)
            except Collections.DoesNotExist as e:
                return self.error_response(code='HTTP_204_NO_CONTENT', message='No data')

            title = request.data.get('title')
            description = request.data.get('description')
            movies = request.data.get('movies')
            if not movies:
                movies = []
            if title:
                collection.title = title
            if description:
                collection.description = description
            collection.save()
            for movie in movies:
                movie_id = movie['id']
                try:
                    selected_movie = Movies.objects.get(id=movie_id, collection_id=collection.id)
                except Movies.DoesNotExist as e:
                    return self.error_response(code='HTTP_204_NO_CONTENT',
                                               message="Movie doesn't exist in your collection")

                if movie.get('title', None):
                    selected_movie.title = movie['title']
                if movie.get('description', None):
                    selected_movie.title = movie['description']
                if movie.get('genres', None):
                    selected_movie.title = movie['genres']
                selected_movie.save()
            return Response({'is_success': True})
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))

    def delete(self, request, collection_id=None):
        """
        Function Name: delete

        Description: delete movies to collection

        Params: title, description, movies

        Return: Updated json

        """
        try:
            user = request.user
            try:
                collection = Collections.objects.get(id=collection_id, user=user)
            except Collections.DoesNotExist as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))
            collection.delete()
            Movies.objects.filter(collection=collection).delete()
            return Response({'is_success': True})
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))
