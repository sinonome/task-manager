from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request を受けたときの動作

def index(request):
    return HttpResponse("Hello, World!")


