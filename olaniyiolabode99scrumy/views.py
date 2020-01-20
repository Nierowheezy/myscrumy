
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView

from olaniyiolabode99scrumy.models import ScrumyGoals

# Create your views here.


def index(request):
    return HttpResponse("This is a Scrum Application")


class ScrumyGoalList(ListView):
    model = ScrumyGoals
