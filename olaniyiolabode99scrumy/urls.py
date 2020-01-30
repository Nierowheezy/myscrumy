from django.contrib.auth import urls
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .views import *
app_name = 'olaniyiolabode99scrumy'
urlpatterns = [
    path('accounts/', include(urls)),
    path('accounts/signup/', sign_up, name='signup'),
    path('addgoal/', add_goal, name='add'),
    path('successpage/', TemplateView.as_view(
        template_name='olaniyiolabode99scrumy/successpage.html'), name='successpage'),
    path('movegoal/<int:goal_id>/', move_view,
         name='movegoal'),  # ex:  /karenzibohscrumy/2/
    path('home/', home, name='home')
]
