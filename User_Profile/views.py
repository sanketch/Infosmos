from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from User_Profile.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.context_processors import csrf
from User_Profile.models import Skill

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid():
        #if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #
            #
            #profile.save()
            registered = True

        else:
            print user_form.errors
            #print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    #return render_to_response(
    #        'register.html',
    #        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
    #        context)
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('../dashboard')
            else:

                return HttpResponse("Your account is disabled.")
        else:

            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render_to_response('login.html', {}, context)

@login_required
def user_dashboard(request):
    context = RequestContext(request)
    return render_to_response('dashboard.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    #return HttpResponse("You are not logged in.")
    return HttpResponseRedirect('../')

@login_required
def user_profile(request):
    context = RequestContext(request)

    if request.method == 'POST':
        listofskills = (request.POST['SkillsList']).split(",")
        #take the string and make it into a list
        #print listofskills
        #iterate through the list and check if the skill in the list is already in the database, if not add it. Then check whether the skill is already added to the user. if not add it.
        for skill in listofskills:
            test = None
            if not Skill.objects.filter(name=skill.lower()):
                newskill = Skill.objects.create(name=skill.lower())
                request.user.profile.skills.add(newskill)
                #print test
            else:
                exists = False
                #print request.user.profile.skills.all()
                for existingSkill in request.user.profile.skills.all():
                    #print existingSkill.name
                    if existingSkill.name == skill.lower():
                        exists = True
                if not exists:
                    newskill = Skill.objects.filter(name=skill.lower())
                    print newskill[0]
                    request.user.profile.skills.add(newskill[0])

        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance = profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('profile.html', args)
