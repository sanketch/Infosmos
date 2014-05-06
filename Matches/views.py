from django.shortcuts import render
from User_Profile.models import Skill, Desire, UserProfile
from Matches.models import Matches
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from User_Profile.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.context_processors import csrf
from User_Profile.models import Skill, Desire
# Create your views here.

def match(request):
    context = RequestContext(request)
    matched = False
    
    if request.method == 'POST':
        match 
        
@login_required
def matches(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    matches = Matches.objects.filter(user1=user)

    return render_to_response('matches.html', {'matches':matches})