import random
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# from django.utila.decorators import method_decorator


from .models import *
# Create your views here.


@login_required(login_url="/olaniyiolabode99scrumy/accounts/login")
def home(request):
    users = User.objects.all()

    def get_by_status(status_name):
        goals = GoalStatus.objects.get(status_name=status_name)
        status_goals = goals.scrumygoals_set.all()
        return status_goals

    daily_goals = get_by_status("Daily Goal")
    weekly_goals = get_by_status("Weekly Goal")
    verify_goals = get_by_status("Verify Goal")
    done_goals = get_by_status("Done Goal")

    dictionary = {
        'users': users,
        'weekly_goals': weekly_goals,
        'daily_goals': daily_goals,
        'verify_goals': verify_goals,
        'done_goals': done_goals,
    }
    return render(request, 'olaniyiolabode99scrumy/home.html', dictionary)


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        data = request.POST.dict()
        user = User.objects.create_user(
            data['username'], data['email'], data['password'])
        user.save()
        new_user = User.objects.get(username=data['username'])
        developer = Group.objects.get(name='Developer')
        developer.user_set.add(new_user)
        response = redirect('/olaniyiolabode99scrumy/successpage/')
        return response
    else:
        form
    return render(request, 'registration/signup.html', {'form': form})


def move_view(request, goal_id):
    dictionary = {"error": "A record with that goal id does not exist"}
    try:
        obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except ScrumyGoals.DoesNotExist:
        return render(request, 'olaniyiolabode99scrumy/exception.html',  dictionary)
    else:
        return HttpResponse(obj.goal_name)


def add_goal(request):
    form = CreateGoalForm
    if request.method == 'POST':
        random_list = list(random.sample(range(1000, 9999), 10))
        random.shuffle(random_list)
        random_no = random_list[0]
        status = GoalStatus.objects.get(status_name="Daily Goal")

        form = form(request.POST)
        data = request.POST.dict()
        user = User.objects.get(id=data['user'])
        add_goal = form.save(commit=False)
        add_goal.goal_id = random_no
        add_goal.goal_status = status
        add_goal.moved_by = user.username
        add_goal.created_by = user.username
        add_goal.owner = user.username
        add_goal.save()
        return HttpResponseRedirect('/olaniyiolabode99scrumy/home')
    context = {
        'create_goal': form
    }

    return render(request, 'olaniyiolabode99scrumy/addgoal.html', context)
