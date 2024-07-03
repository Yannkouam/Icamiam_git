from django.db import models
from django.contrib.auth.models import AbstractUser


class Shopper(AbstractUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='username')
    password = models.CharField(max_length=128, verbose_name='password')
    def __str__(self):
        return self.username
