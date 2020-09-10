from django.conf.urls import url
from .views import (
    GetMovies, MovieCollection
)

urlpatterns = [
    url(r'^movies/$', GetMovies.as_view(), name='movies'),
    url(r'^collection/$', MovieCollection.as_view(), name='collection'),
    url(r'^collection/(?P<collection_id>[0-9a-zA-Z]+)/$', MovieCollection.as_view(), name='collection-mod'),

]