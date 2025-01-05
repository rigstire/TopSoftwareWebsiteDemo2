from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    company_name = models.CharField(max_length=25, unique=False)

    def __str__(self):
        return self.username
