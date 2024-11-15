from django.urls import path
from .views import role_selection, TeacherSignUpView, StudentSignUpView
from . import views



#app_name = 'users'

urlpatterns = [
    path('signup/', role_selection, name='role_selection'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
