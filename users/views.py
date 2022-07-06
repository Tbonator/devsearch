from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.


def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("username doesnt exist")
        # check if yhe user exists in DB
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login() will create a session for the use and add that into cookies
            login(request, user)
            return redirect('profiles')
        else:
            print("Username OR Password is Incorrect")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
    


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # exclude  topskill with empty description
    topSkills = profile.skill_set.exclude(description__exact="")
    # exclude  otherskill with empty description
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
