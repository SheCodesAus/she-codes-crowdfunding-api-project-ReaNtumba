from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField()
    image = models.URLField()
    # delete_profile = models.deletion() 

    def __str__(self):
        return self.username