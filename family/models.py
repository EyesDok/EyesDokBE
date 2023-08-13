from django.db import models
from accounts.models import CustomUser

class Family(models.Model):
    familyname = models.CharField(max_length=100)
    members = models.IntegerField(null=True)
    users = models.ManyToManyField(CustomUser, related_name='families')
    class Meta:
        db_table='family'

    def __str__(self):
        return self.family_name