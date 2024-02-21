"""
Models of the core application.
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    """Custom user manager for the application."""

    def create_user(self, email: str, password: str = None, **extra_fields):
        """
        Creates and saves a user with the given email address and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model for the application."""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_staff
