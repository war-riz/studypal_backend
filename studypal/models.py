from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=50, unique=True)  # Unique Student ID
    full_name = models.CharField(max_length=255)  # Full Name
    course_of_study = models.CharField(max_length=255, blank=True, null=True)  # Course of Study
    gender = models.CharField(
        max_length=10,
        choices=[('Boy', 'Boy'), ('Girl', 'Girl')],
    )  # Gender Selection
    user_type = models.CharField(
        max_length=10,
        choices=[('Growing', 'Growing'), ('Elite', 'Elite')],
    )  # User Type (Growing or Elite)

    def __str__(self):
        return self.full_name


