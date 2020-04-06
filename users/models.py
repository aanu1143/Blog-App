from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fruit= models.CharField(max_length=100,choices=(('mango','Mango'),('apple','Apple')))
    age = models.PositiveIntegerField(null=True, blank=True)