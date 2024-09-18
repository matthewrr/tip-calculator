from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

#AVATAR

class CustomUser(AbstractUser):
    preferred_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    ROLE_CHOICES = [
        ("BARTENDER", "Bartender"),
        ("BARBACK", "Barback"),
        ("SECURITY", "Security"),
        ("OTHER", "Other"),
    ]
    default_role = models.CharField(
        max_length=30,
        choices = ROLE_CHOICES,
    )
    created_date = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=30, blank=True)

    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        if self.preferred_name:
            #code for preferred or first assignmemt
            return f"{self.preferred_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"