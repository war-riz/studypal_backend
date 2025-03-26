from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser model"""

    def create_user(self, matricNumber, fullName, course, gender, role, password=None):
        """Create and return a regular user with the given details."""
        if not matricNumber:
            raise ValueError("Matric Number is required for students")

        if CustomUser.objects.filter(matricNumber=matricNumber).exists():
            raise ValueError("A user with this Matric Number already exists.")

        user = self.model(
            matricNumber=matricNumber,
            fullName=fullName,
            course=course,
            gender=gender,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricNumber, email, password):
        """Create and return a superuser with matricNumber, email, and password."""
        if not email:
            raise ValueError("Superuser must have an email address")
        if not matricNumber:
            raise ValueError("Superuser must have a matricNumber")
        if not password:
            raise ValueError("Superuser must have a password")

        superuser = self.model(
            matricNumber=matricNumber,
            email=self.normalize_email(email),
            is_staff=True,
            is_superuser=True
        )
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser


class CustomUser(AbstractUser):
    """Custom user model"""
    username = None  # Remove default username field
    matricNumber = models.CharField(max_length=50, unique=True)

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

    USERNAME_FIELD = "matricNumber"  # Use matricNumber for login
    REQUIRED_FIELDS = ["email"]  # Keep email required for superusers

    def __str__(self):
        if self.is_superuser:
            return f"admin_{self.matricNumber}"
        return f"{self.fullName} ({self.matricNumber})" if self.fullName else self.matricNumber

