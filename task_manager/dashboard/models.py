from django.db import models

class Account(models.Model):
    # NOTE: primary key は必要ない？
    # https://docs.djangoproject.com/ja/4.1/topics/db/models/#automatic-primary-key-fields
    # user_id = models.IntegerF
    user_id     = models.BigAutoField(primary_key=True)
    user_name   = models.TextField()
    passwd      = models.TextField()

class Goal(models.Model):
    # NOTE: 目標
    goal_id     = models.BigAutoField(primary_key=True)
    user        = models.ForeignKey(Account, on_delete=models.CASCADE)
    goal_name   = models.TextField()

class Task(models.Model):
    # NOTE: Main and sub Task
    task_id         = models.BigAutoField(primary_key=True)
    goal            = models.ForeignKey(Goal, on_delete=models.CASCADE)
    parent          = models.ForeignKey("self", on_delete=models.CASCADE)
    task_name       = models.TextField()
    schedule_date   = models.DateTimeField()
    schedule_time   = models.PositiveIntegerField()
    record_date     = models.DateTimeField()
    record_time     = models.PositiveIntegerField()
    task_details    = models.TextField()
