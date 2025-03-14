from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    usericon = models.ImageField(
        upload_to="usericons/",
        default="usericons/default.png",
        blank=True
    )
    def __str__(self):
        return self.username