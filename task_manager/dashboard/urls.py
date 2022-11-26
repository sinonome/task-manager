from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('task-form', views.task_form, name="regist task"),
    path('Test2', views.Test2, name="dashboard"),
    path('Test3', views.Test3, name="dashboard"),
    path('TestPage', views.TestPage, name="hello")
]
