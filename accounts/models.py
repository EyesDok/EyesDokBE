from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    membership = models.CharField(max_length=150,default=False)

    def __str__(self):
        return self.username
