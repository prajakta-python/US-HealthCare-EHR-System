from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import UserManager


class User(AbstractUser):
    """Custom user model that logs in with email instead of username."""

    # All possible roles in the system (RBAC foundation)
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        NURSE = "NURSE", "Nurse"
        PATIENT = "PATIENT", "Patient"
        INTEGRATION = "INTEGRATION", "Integration User"

    # Remove username field; email will be the login identifier
    username = None
    email = models.EmailField("email address", unique=True)

    # Which role this user has
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT,
    )
    phone = models.CharField(max_length=20, blank=True)

    # Tell Django to use email (not username) for authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []      # email + password are already required

    # Use our custom manager
    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"
