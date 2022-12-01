from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render  
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
# from .models import Post
# from .models import Member
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import LoginModel ,CoursesModel ,StudentModel
from .forms import LoginForm ,StudentForm



def home(request):
    # if request.method == 'POST' :
    # title = request.POST['title']
    reg= request.POST.get("reg", "Enter Reg Number")
    password= request.POST.get("password", "password")
    # description = request.POST['description']
    form = LoginForm(request.POST or None)
    print(f"Login:{reg} {password} ")
    context ={}
    if reg != "Enter Reg Number" and password != "password" and form.is_valid() and request.method == 'POST'  :
        print("What has been posted:" , request.POST)
        reg_num = LoginModel.objects.filter(reg=reg).values("reg")
        if "signup" in request.POST:

            if (len(reg_num)!=0):
                return HttpResponse( "<script>alert('Registration number already taken.');window.location.href = 'home';;</script>")
            else : 
                form.save()
                response =HttpResponseRedirect("login")
        # context["dataset"] = LoginModel.objects.all()
                print("Password: ",password)
                response.set_cookie(
                    "isloggedin",
                    reg,
                    max_age=365 * 24 * 60 * 60,
                   
                )
                return response
        elif "signin" in request.POST:
            try:
                reg_num = LoginModel.objects.get(reg=reg)
                response =HttpResponseRedirect("login")
                response.set_cookie(
                        "isloggedin",
                        reg,
                        max_age=365 * 24 * 60 * 60,
                        
                    )
                response =HttpResponseRedirect("login")
                response.set_cookie(
                        "isloggedin",
                        reg,
                        max_age=365 * 24 * 60 * 60,
                        
                    )
            
                return response
            except Exception as e :

                return HttpResponse( "<script>alert('No such login details');window.location.href = 'home';;</script>")
    else:
        
        loggedin = request.COOKIES.get('isloggedin')
        print(loggedin)
        if loggedin == None:
            context["login"] = "Sign In"
            return render(request, "index.html",context)
        else:
            context["login"] = "Signed In As "+ loggedin
            return render(request, "index.html",context)

def degree_programs(request):
    context ={}
    loggedin = request.COOKIES.get('isloggedin')
        
    if loggedin == None:
        context["login"] = "Sign In"
    else:
        context["login"] = "Your are logged in as "+ loggedin
    print("Logged: " ,loggedin)
    return render(request, "degree_programs.html",context)

def register_course(request):
    # return render(request, "degree_programs.html")
    course_id= request.POST.get("register", "no_id")
    print(course_id)
    # context = {}
    if course_id != "no_id":
        
        course = CoursesModel.objects.get(id=course_id)
        print(course.__dict__)
        print("#######################")
        print(course)
        
        data = {
        
			"course_name":course.course_name,
			"course_id":course.course_id,
			"lecturer":course.lecturer,
			"picture":course.picture,
			"rating":course.rating,
			"assignment":course.assignment,
			"due_date":course.due_date,
			"grading":course.grading,
			"description":course.description,
			"student_id":request.COOKIES.get('isloggedin')
       }
        form = StudentModel(**data)
        form.save()
        data = StudentModel.objects.filter(student_id=request.COOKIES.get('isloggedin'))
        context ={} 
        context['con']= data
        
    
    return render(request, "student-dashboard-my-courses.html",context)


def dashboard_courses(request):
    context ={}
    loggedin = request.COOKIES.get('isloggedin')
        
    if loggedin == None:
        context["login"] = "Sign In"
    else:
        context["login"] = "Your are logged in as "+ loggedin
    print("Logged: " ,loggedin)

       

    # add the dictionary during initialization
    
    
    context["courses"] = CoursesModel.objects.all()
    return render(request, "dashboard_courses.html",context)

def login(request):
    return render(request, "login.html")

def upload(request):
    return render(request, "upload.html")


def student_dashboard(request):
    data = StudentModel.objects.filter(student_id=request.COOKIES.get('isloggedin'))
    context ={} 
    loggedin = request.COOKIES.get('isloggedin')
        
    context["login"] = "Your are logged in as "+ loggedin
    print("Logged: " ,loggedin)
    context['con']= data
    return render(request, "student-dashboard-my-courses.html",context)

# relative import of forms

 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    

 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    context["dataset"] = LoginModel.objects.all()
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)


