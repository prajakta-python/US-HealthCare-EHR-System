from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Custom manager: create users using email instead of username."""

    def create_user(self, email, password=None, **extra_fields):
        # Email is mandatory for every user
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)          # lowercase the domain part
        user = self.model(email=email, **extra_fields)
        user.set_password(password)                  # store the password hashed, never plain
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # A superuser must have these flags set to True
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "ADMIN")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)
