from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
