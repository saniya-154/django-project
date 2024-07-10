from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want to store
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)

def __str__(self):
    return self.user.username