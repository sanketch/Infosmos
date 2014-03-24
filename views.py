from django.shortcuts import render_to_response
from django.http import HttpResponceRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#csrf is a security stamp to stop Haxors submitting fake forms


def login(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password = password)

    if user is not None:
        auth.login(request, User)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

    

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})
def invalid_login(request):
    auth.logout(request)
    return render_to_response('logout.html')
