from django.db import models


class RequestLogger(models.Model):
    """
       Model class for manage user details.
    """
    id = models.IntegerField(primary_key=True, default=1)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'request_logger'
