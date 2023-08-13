from django.db import models
from django.contrib.auth.models import AbstractUser

class FamilyGroup(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField('CustomUser', related_name='families')

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    membership = models.CharField(max_length=150, default=False)
    family = models.ForeignKey(FamilyGroup, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.username
