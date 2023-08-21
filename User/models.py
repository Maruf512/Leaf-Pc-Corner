from django.db import models


# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=50, null=False)
    u_password = models.CharField(max_length=30, null=False)
