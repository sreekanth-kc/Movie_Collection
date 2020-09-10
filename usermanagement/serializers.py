from rest_framework import serializers
from usermanagement.models import AppUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['password', 'username', 'id']
        extr_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = AppUser(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
