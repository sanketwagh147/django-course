from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)  # is optional field
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self) -> str:
        return str(self.user.username)
