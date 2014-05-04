from django.shortcuts import render
from User_Profile.models import Skills, Desires, Askill, Adesire,UserProfile
from Matches.models import Match
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def match(request):
    context = RequestContext(request)
    matched = False
    
    if request.method == 'POST':
        match 
 
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#  
#  
#             profile.save()
#             registered = True