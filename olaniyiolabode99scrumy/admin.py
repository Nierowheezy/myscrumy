from django.contrib import admin
from . models import GoalStatus
from . models import ScrumyHistory
from . models import ScrumyGoals
from . models import User


# Register your models here.
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)

