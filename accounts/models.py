from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('employee','Employee')
    )

    role = models.CharField(max_length=20, choices=USER_ROLES, default='manager')
    last_activity = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField( upload_to="images",  blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.email + " - " + self.role.upper()
