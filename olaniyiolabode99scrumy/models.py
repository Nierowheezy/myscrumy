from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User():
#     User = get_user_model()


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=100)


class ScrumyGoals(models.Model):
    user = models.ForeignKey(User, related_name='goals',
                             on_delete=models.CASCADE)
    goal_id = models.IntegerField()
    goal_name = models.CharField(max_length=100)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=100)
    moved_by = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)


class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT, default=0.0)
    moved_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    moved_from = models.CharField(max_length=100)
    moved_to = models.CharField(max_length=100)
    time_of_action = models.DateField()
