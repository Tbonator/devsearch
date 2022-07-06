from .models import Profile
from django.shortcuts import render

# Create your views here.
def profiles (request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    # exclude  topskill with empty description
    topSkills = profile.skill_set.exclude(description__exact="")
    # exclude  otherskill with empty description
    otherSkills = profile.skill_set.filter(description = "")
    
    context = {'profile': profile, 'topSkills': topSkills,'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
