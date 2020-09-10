from django.conf.urls import url
from request_logger.views import (
    LogRequest
)

urlpatterns = [
    url(r'^request-count$', LogRequest.as_view(), name='request-count'),
    url(r'^request-count/reset$', LogRequest.as_view(), name='reset-request-count')
]
