from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField("Correo electrónico", unique=True, blank=False)
    # Avatar field
    avatar = models.ImageField(
        upload_to='avatars/',  # folder inside MEDIA_ROOT
        null=True,
        blank=True,
        verbose_name="Avatar",
        default = 'avatars/default.jpg'
    )

    def __str__(self):
        return self.username

