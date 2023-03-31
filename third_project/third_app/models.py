from django.db import models


# Create your models here.
class User(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True, default=None)
