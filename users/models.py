


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    telegram_username = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username