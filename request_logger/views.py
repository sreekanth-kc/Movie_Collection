from rest_framework.views import APIView
from rest_framework.response import Response
from request_logger.models import RequestLogger
from utilities.mixins import HttpResponseMixin
from django.db import transaction
from rest_framework.permissions import IsAuthenticated


class LogRequest(APIView, HttpResponseMixin):
    """
    Class Name: LogRequest

    Description: Manage Logging activity
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Function Name: get

        Description: Get request count

        Params: Nil

        Return: request count
        """
        try:
            with transaction.atomic():

                counter_data = RequestLogger.objects.select_for_update().get(id=1)
                return Response({'requests': counter_data.count})
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))

    def post(self, request):
        """
        Function Name: post

        Description: Reset request count

        Params: Nil

        Return: Nil
        """
        try:
            with transaction.atomic():
                counter_data = RequestLogger.objects.select_for_update().get(id=1)
                counter_data.count = 0
                counter_data.save()
                return Response({'message': 'request count reset successfully'})
        except Exception as e:
            return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))
