from django.contrib.auth.models import AbstractUser
from django.db import models

# same as abstract user with age field added
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)

    
