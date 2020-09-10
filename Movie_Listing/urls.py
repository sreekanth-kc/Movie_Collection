from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('usermanagement.urls')),
    path('', include('request_logger.urls')),
    path('', include('user_movie_collection.urls')),
    path('admin/', admin.site.urls),
]
