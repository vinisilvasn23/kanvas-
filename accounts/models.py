from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
