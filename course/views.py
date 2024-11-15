# views.py
from django.shortcuts import render
from .models import Course
from django.urls import reverse

def new_course(request):
    title = request.POST['title']
    description = request.POST['description']
    print(title,description,"gtgnldgnlk")
    #student = Student.objects.create(name="John Doe", email="john@example.com")
    #course1 = allcourses.objects.create(title="Mathematics", description="Math course")
    #course2 = allcourses.objects.create(title="Science", description="Science course")
    #student.courses.add(course1, course2)
    #return redirect('dash')
    return render(request, 'course/dashboard.html')

def course_detail(request, course_id):
    course = Course.objects.get(title=course_id)
        #instructor = course.instructors.first()  # Assuming one instructor per course
    context = {
        'course': course,
    }
    return render(request, 'course/course_detail.html', context)

def dash(request):
    det = reverse('course:course_detail', kwargs={'course_id': 'placeholder'}).replace('placeholder/', '')
    edit = reverse('course:course_edit', kwargs={'course_id': 'placeholder'}).replace('placeholder/', '')
    
    if request.method == 'POST': 
        title = request.POST['title'] 
        description = request.POST['description']
        print(request)
        #try Course.objects.get(title=title):
         #   print("error")
          ##  courses = Course.objects.all()
            #return render(request, 'course/dashboard.html', {'course':courses})
        #except Er
        

        print(title,"thdggf")
        student = Course.objects.create()
        student.title = title
        student.description = description
        student.save()
        
        courses = Course.objects.all()
        return render(request, 'course/dashboard.html', {'course':courses, 'edit':edit, 'detail':det})
    else:
        courses = Course.objects.all()
        return render(request, 'course/dashboard.html', {'course':courses, 'edit':edit, 'detail':det})


    if request.user.is_authenticated:
        profession = request.user.profession
        print(profession)  # Outputs: 'Teacher', 'Student', or 'Unknown'    
        if profession =="Student":
            return render(request, "course/dashboard.html")
        else:
            n = "no of students"
            return render(request, "course/dashboard.html", {"stu": n})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Course

def course_edit(request, course_id):
    course = get_object_or_404(Course, title=course_id)
    print("fuck")
    if request.method == 'POST':
        print("fuck twice")
        course.title = request.POST['title']
        print("course.title")
        course.overview = request.POST['overview']
        course.outline = request.POST['outline']
        course.description = request.POST['description']
        course.duration = request.POST['duration']
        course.level = request.POST['level']
        course.prerequisites = request.POST['prerequisites']
        course.instructor_name = request.POST['instructor_name']
        course.instructor_bio = request.POST['instructor_bio']
        if 'instructor_picture' in request.FILES:
            course.instructor_picture = request.FILES['instructor_picture']
        course.save()
        return JsonResponse({'status': 'success'})
    
    return render(request, 'course/editable.html', {'course': course})
