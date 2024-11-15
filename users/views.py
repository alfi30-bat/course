# Project structure:
# myproject/
#   manage.py
#   myproject/
#     __init__.py
#     settings.py
#     urls.py
#     wsgi.py
#   users/
#     __init__.py
#     admin.py
#     apps.py
#     forms.py
#     models.py
#     urls.py
#     views.py
#   templates/
#     base.html
#     home.html
#     users/
#       login.html
#       signup.html
#       role_selection.html
#       teacher_signup.html
#       student_signup.html


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import TeacherSignUpForm, StudentSignUpForm
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import LoginForm

def home(request):
    return render(request, 'course/main3.html')

def role_selection(request):
    return render(request, 'users/role_selection.html')

class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'users/teacher_signup.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        print(user,"gdfgdfg",self)
        return redirect('login')

class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'users/student_signup.html'

    def form_valid(self, form):
        user = form.save()
        print(self)
        #login(self, user)
        return redirect('login')



def login_view(request):
    # In a view
    if request.user.is_authenticated:
        profession = request.user.profession
        print(profession)  # Outputs: 'Teacher', 'Student', or 'Unknown'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')  # redirect to your desired page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})  # Use a dict here

def logout_view(request):
    logout(request)
    return redirect('main')


