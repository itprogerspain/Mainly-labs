from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Custom manager to handle user and superuser creation
class CustomManagerUser(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("role", "superadmin")
        return super().create_superuser(username, email, password, **extra_fields)


# Extended user model
