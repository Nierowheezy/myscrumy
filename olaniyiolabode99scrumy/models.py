from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User():
#     User = get_user_model()


class ScrumyGoals(models.Model):
    goal_id = models.primary_key = True
    goal_status = models.ForeignKey('GoalStatus', on_delete=models.PROTECT)
    created_by = models.DateField()
    moved_by = models.DateTimeField()
    owner = models.TextField()
    goal_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class ScrumyHistory(models.Model):
    moved_by = models.DateTimeField()
    created_by = models.DateField()
    moved_from = models.DateTimeField()
    moved_to = models.DateTimeField()
    time_of_action = models.TimeField()


class GoalStatus(models.Model):
    # goal_status = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
    status_name = models.TextField()
