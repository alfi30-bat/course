# urls.py (in your app's urls.py file)
from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('course/<str:course_id>/', views.course_detail, name='course_detail'),
    path('course_edit/<str:course_id>/', views.course_edit, name='course_edit'),
    path('dashboard/', views.dash, name='dash'),
    path('dashboard/new', views.new_course, name='n_course')
]