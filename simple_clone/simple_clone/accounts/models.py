from django.db import models
from django.contrib import auth
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your models here.


class User(auth.models.User, PermissionRequiredMixin):
    def __str__(self):
        return f"@{self.username}"
