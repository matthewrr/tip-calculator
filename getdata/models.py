from django.db import models
from django.utils import timezone

# class Employee(models.Model):
#     active = models.BooleanField(default=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     preferred_name = models.CharField(max_length=30, blank=True)
#     ROLE_CHOICES = [
#         ("BARTENDER", "Bartender"),
#         ("BARBACK", "Barback"),
#         ("SECURITY", "Security"),
#         ("OTHER", "Other"),
#     ]
#     default_role = models.CharField(
#         max_length=30,
#         choices = ROLE_CHOICES,
#     )
#     created_date = models.DateTimeField(default=timezone.now)
#     email_address = models.EmailField(max_length=254, blank=True)
#     phone_number = models.CharField(max_length=30, blank=True)
    # access_level (make list of privies)
    #change_log
    #image

    # def __str__(self):
    #     if self.preferred_name:
    #         #code for preferred or first assignmemt
    #         return f"{self.preferred_name} {self.last_name}"
    #     else:
    #         return f"{self.first_name} {self.last_name}"