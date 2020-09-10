import time
from django.utils.deprecation import MiddlewareMixin
from request_logger.models import RequestLogger
from django.db import transaction


class RequestLogMiddleware(MiddlewareMixin):
    """Request Logging Middleware."""

    def process_request(self, request):
        with transaction.atomic():
            try:
                counter_data = RequestLogger.objects.select_for_update().get(id=1)
            except RequestLogger.DoesNotExist:
                counter_data = None

            if counter_data:
                counter_data.count = counter_data.count + 1
                counter_data.save()
            else:
                new_data = RequestLogger(id=1, count=1)
                new_data.save()
