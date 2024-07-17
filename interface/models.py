from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    # Add additional fields here
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Add any other fields or custom methods if needed
    def __str__(self):
        return self.username