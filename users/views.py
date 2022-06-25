from .models import Profile
from django.shortcuts import render

# Create your views here.
def profiles (request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile }
    return render (request, 'users/user-profile.html',context)
