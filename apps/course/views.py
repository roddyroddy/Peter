from django.shortcuts import render, HttpResponse, redirect
from .models import Course

from apps.course.models import *

def index(request):
    b = Course.objects.all()
    
    return render(request, 'course/index.html', {"course":b})

def new(request):
    add = Course.objects.create(course_name = request.POST['course_name'], description = request.POST['description'])
    
    return redirect('/')

def delete(request, id):
    transfer = {"course" : Course.objects.filter(id = id).values()}  
    print(transfer)  

    return render(request, 'course/destroy.html', transfer)

def destroy(request, id):
    d = Course.objects.get(id = id)
    d.delete()
    print("------------------------------------",d)

    return redirect('/')