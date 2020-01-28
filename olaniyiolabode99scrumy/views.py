
from django.shortcuts import render
from django.http import HttpResponse
import random
from olaniyiolabode99scrumy.models import GoalStatus, ScrumyGoals, ScrumyHistory
from django.contrib.auth.models import User
from django.template import loader

# Create your views here.
# goal = ScrumyGoals.objects.get(goal_id)
# number = list(range(1000, 10000)


def get_grading_parameters(request):
    all_goals = ScrumyGoals.objects.get(pk=1)
    goal = all_goals.goal_name
    # goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)


def move_goal(request, goal_id):
    # goal = ScrumyGoals.objects.get(goal_id=goal_id)
    try:
        goal = ScrumyGoals.objects.get(goal_id=goal_id)
        return HttpResponse(goal)
    except:
        context = {
            "error": "A record with that goal id does not exist"
        }
        return render(request, "olaniyiolabode99scrumy/exception.html", context)
    # return HttpResponse(goal)
    # return HttpResponse("You are getting the goal %s. " % goal_id)


def add_goal(request):
    randomGoalId = random.randint(1000, 9999)
    WeeklyGoal = GoalStatus.objects.get(status_name="Weekly Goal")
    user = User.objects.get(username="louis")
    goal = ScrumyGoals(goal_name="Keep Learning Django", goal_id=randomGoalId, created_by="Louis",
                       moved_by="Louis", owner="Louis", goal_status=WeeklyGoal, user=user)
    goal.save()
    return HttpResponse("User and Goal Created Successfully")


def home(request):
    # goal = ScrumyGoals.objects.get(goal_name="Keep Learning Django")
    # output = ', '.join([goal.goal_name for goal in goal])
    # display_val = goal.goal_name
    # return HttpResponse(display_val)
    # return HttpResponse(ScrumyGoals.objects.filter(goal_name="keep Learning Django"))
    goal = ScrumyGoals.objects.get(goal_name="Learn Django")
    user = User.objects.get(username="louis oma")
    # template = loader.get_template("olaniyiolabode99scrumy/home.html")
    dictionary = {
        "goal_name": goal.goal_name,
        "goal_id": goal.goal_id,
        "user": user
    }
    # return HttpResponse(template.render(dictionary, request))
    return render(request, "olaniyiolabode99scrumy/home.html", dictionary)


def goal_name(request):
    # goal_name = ScrumyGoals.objects.order_by('-pub_date')
    goal = ScrumyGoals.objects.get(goal_name="Keep Learning Django")
    output = ', '.join([goal.goal_name for goal in goal])
    return(output)
