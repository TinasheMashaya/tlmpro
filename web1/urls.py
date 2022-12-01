"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import  home ,degree_programs ,student_dashboard ,login ,upload ,create_view,dashboard_courses ,register_course
from django.urls import include, re_path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('home',home,name='home'),
    path('degree_programs/',degree_programs ,name= 'degree_programs'),
    path('student_dashboard/',student_dashboard,name='student_dashboard'),
    path('login/',login,name='login'),
    path('upload/',upload,name='upload'),
    path('create_view/',create_view,name='create_view'),
    path('dashboard_courses/',dashboard_courses,name='dashboard_courses'),
    path("register_course/", register_course ,name="register_course"),
    
    
    # url(r'^insert$', views.insert, name='insert'),
    # re_path(r'form', views.my_form, name='form')
    
    
]
