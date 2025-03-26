from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    matricNumber = models.CharField(max_length=50, unique=True)  # Unique Student ID
    fullName = models.CharField(max_length=255)  # Full Name
    course = models.CharField(max_length=255, blank=True, null=True)  # Course of Study
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')],
    )  # Gender Selection
    role = models.CharField(
        max_length=10,
        choices=[('Growing', 'Growing'), ('Elite', 'Elite')],
    )  # User Type (Growing or Elite)

    def __str__(self):
        return self.full_name


