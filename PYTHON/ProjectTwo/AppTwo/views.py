from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    return HttpResponse('<em>My second app</em>')


def help(request):
    context = {'help_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'}
    return render(request,'apptwo/help.html',context=context)

def users(request):
    users_list = models.User.objects.all()
    context = {'users_list':users_list}
    return render(request, 'apptwo/users.html',context=context)
