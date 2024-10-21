from django.shortcuts import render
from .models import Profile


def home(request):  
    return render(request, 'index.html')  



def profile_view(request):
    profile = Profile.objects.filter()
    return render(request, 'profile.html',{"profile":profile})