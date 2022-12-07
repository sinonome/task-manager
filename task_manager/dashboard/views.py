from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request を受けたときの動作

def index(request):
    return render(request, "dashboard/index.html")

def task_form(request):
    return render(request, "form/index.html")

def record_study(request):
    return render(request, "form/record.html")

def schedule(request):
    return render(request, "form/schedule.html")

def Test2(request):
    return HttpResponse("Hello, Test2!")

def Test3(request):
    return HttpResponse("Hello, Test3!")

def TestPage(request):
    return render(request, "testpage/TestPage.html")
