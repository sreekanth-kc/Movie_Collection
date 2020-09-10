from rest_framework.views import APIView
from rest_framework.response import Response
from utilities.mixins import HttpResponseMixin
from usermanagement.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class Register(APIView, HttpResponseMixin):
    """
    Class Name: Register

    Description: Manage user registration
    """

    def post(self, request):
        """
        Function Name: post

        Description: User registration

        Params: username, password

        Return: access_token
        """
        if request.method == 'POST':
            try:
                serializer = RegistrationSerializer(data=request.data)
                data = {}
                if serializer.is_valid():
                    account = serializer.save()
                    encoded_jwt = RefreshToken.for_user(account)
                    data['access_token'] = str(encoded_jwt.access_token)
                else:
                    data = serializer.errors
                return Response(data)
            except Exception as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))

