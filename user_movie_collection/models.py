import uuid
from django.db import models


class Collections(models.Model):
    """
    Model class for manage user details.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    user = models.ForeignKey("usermanagement.Appuser", blank=True, null=True,
                             related_name='user', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'collections'


class Movies(models.Model):
    """
    Model class for manage user details.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    genres = models.CharField(max_length=255, null=True)
    collection = models.ForeignKey(Collections, blank=True, null=True,
                                   related_name='collection', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'movies'
