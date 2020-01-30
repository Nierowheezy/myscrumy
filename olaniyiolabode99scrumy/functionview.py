from django.http import HttpResponse, Http404, HttpResponseRedirect

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

    def success_page(request):
    return render(request, 'olaniyiolabode99scrumy/successpage.html')


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        data = request.POST.dict()
        form.save()
        username = data['username']
        new_user = User.objects.get(username=username)
        developer = Group.objects.get(name='Developer')
        developer.user_set.add(new_user)
        return HttpResponseRedirect('/olaniyiolabode99scrumy/successpage')
    else:
        form
    return render(request, 'registration/signup.html', {'form': form})
