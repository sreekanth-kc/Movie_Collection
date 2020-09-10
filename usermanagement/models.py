import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from Movie_Listing import settings
import jwt


class AppUser(AbstractUser):
    """
       Model class for manage user details.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'
