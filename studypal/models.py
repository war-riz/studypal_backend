from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser model"""

    def create_user(self, matricNumber, fullName, course, gender, role, password=None):
        """Create and return a regular user with the given details."""
        if not matricNumber:
            raise ValueError("Matric Number is required for students")

        user = self.model(
            matricNumber=matricNumber,
            fullName=fullName,
            course=course,
            gender=gender,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """Create and return a superuser with username, email, and password."""
        if not email:
            raise ValueError("Superuser must have an email address")
        if not username:
            raise ValueError("Superuser must have a username")
        if not password:
            raise ValueError("Superuser must have a password")

        superuser = self.model(
            username=username,
            email=self.normalize_email(email),
            is_staff=True,
            is_superuser=True
        )
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser


class CustomUser(AbstractUser):
    """Custom user model"""
    matricNumber = models.CharField(max_length=50, unique=True, blank=True, null=True)
    fullName = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        blank=True, null=True
    )
    role = models.CharField(
        max_length=10,
        choices=[('Growing', 'Growing'), ('Elite', 'Elite')],
        blank=True, null=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        if self.fullName and self.matricNumber:
            return f"{self.fullName} ({self.matricNumber})"
        return self.username  # Fallback for superusers

