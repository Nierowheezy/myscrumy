from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Create your models here.

class GoalStatus(models.Model):
    status_name = models.TextField(default=None)

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.TextField(default=None)
    goal_id = models.IntegerField(default=None)
    created_by = models.TextField(default=None)
    moved_by = models.TextField(default=None)
    owner = models.TextField(default=None)
    user = models.ForeignKey(
        User, related_name='user_name', on_delete=models.PROTECT)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by = models.TextField(default=None)
    created_by = models.TextField(default=None)
    moved_from = models.TextField(default=None)
    moved_to = models.TextField(default=None)
    time_of_action = models.TextField(default=None)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)

    def __str__(self):
        return self.created_by


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
