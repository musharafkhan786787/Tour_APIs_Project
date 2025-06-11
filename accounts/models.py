from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Enforce unique emails
    USERNAME_FIELD = 'email'               # Use email to login
    REQUIRED_FIELDS = ['username']         # username is optional

    def __str__(self):
        return self.email