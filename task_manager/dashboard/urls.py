from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('Test1', views.Test1, name="dashboard"),
    path('Test2', views.Test2, name="dashboard"),
    path('Test3', views.Test3, name="dashboard"),
    path('TestPage', views.TestPage, name="hello")
]
