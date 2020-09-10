"""
File Name: mixins.py

Description: Define custom mixins
"""
from rest_framework import status
from rest_framework.response import Response


class HttpResponseMixin(object):
    """
    Class Name: ResponseViewMixin

    Description: Define response formatting methods
    """

    @classmethod
    def success_response(self, code='HTTP_200_OK', message=None, data=None):
        """
        Function Name: success_response

        Description: Return formatted success response

        Input:
        code - string - HTTP status code
        data - json - json data to be returned

        Output:
        Formatted json
        """
        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': message,
                'status': getattr(status, code),
                'data': data
            },
            content_type='application/json'
        )

    @classmethod
    def error_response(self, code=None, message=None, data=None):
        """
        Function Name: error_response

        Description: Return formatted error response

        Input:
        code - string - HTTP status code
        data - json - json data to be returned

        Output:
        Formatted json
        """
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'status': getattr(status, code),
                'message_list': message
            },
            content_type='application/json'
        )
