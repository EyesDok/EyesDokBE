from django.db import models
from accounts.models import CustomUser

class Family(models.Model):
    family_name = models.CharField(max_length=100)
    members_count = models.PositiveIntegerField()
    users = models.ManyToManyField(CustomUser, related_name='families')

    def __str__(self):
        return self.family_name