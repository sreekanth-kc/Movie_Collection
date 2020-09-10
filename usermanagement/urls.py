from django.conf.urls import url
from usermanagement.views import (
    Register
)

urlpatterns = [
    url(r'^register', Register.as_view(), name='register')
]
