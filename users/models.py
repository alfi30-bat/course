# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    resume_link = models.URLField(blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)

    @property
    def profession(self):
        if self.is_teacher:
            return 'Teacher'
        elif self.is_student:
            return 'Student'
        else:
            return 'Unknown'
