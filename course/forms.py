# forms.py
from django import forms
from course.models import Course, Instructor,allcourses,Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','overview', 'description', 'duration', 'level', 'prerequisites']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'title', 'bio', 'image']

