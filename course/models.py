# models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200 , default="null")
    overview = models.TextField(default="null")
    outline = models.TextField(default="null")
    description = models.TextField(default="null")
    duration = models.IntegerField(default=1)
    level = models.CharField(max_length=50,default="null")
    prerequisites = models.TextField(default="null")
    instructor_name = models.CharField(max_length=100,default="null")
    instructor_picture = models.ImageField(upload_to='instructors', null=True, blank=True,default="null")
    instructor_bio = models.TextField(default="null")


