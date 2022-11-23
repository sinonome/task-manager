from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request を受けたときの動作

def index(request):
    return render(request, "dashboard/index.html")

def Test1(request):
    return HttpResponse("Hello, Test1!")

def Test2(request):
    return HttpResponse("Hello, Test2!")

def Test3(request):
    return HttpResponse("Hello, Test3!")
