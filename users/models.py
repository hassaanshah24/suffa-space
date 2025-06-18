# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Choices for user type
USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('faculty', 'Faculty'),
    ('student', 'Student'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    department = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
