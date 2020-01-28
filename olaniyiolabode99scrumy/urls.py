"""myscrummy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_grading_parameters, name="index"),
    path('movegoal/<int:goal_id>/', views.move_goal, name="movegoal"),
    path('addgoal/', views.add_goal, name="addgoal"),
    path('home/', views.home, name="home"),
    path('goalname/', views.goal_name, name="goalname")
]
