from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
class User(AbstractUser):
    username = None
    email = models.CharField(max_length=100,unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email