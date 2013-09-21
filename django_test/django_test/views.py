from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
# for registration
from forms import MyRegistrationForm


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    # check if this user exist within the system and password matched
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        # we want this user to be in our system as "loggedin" now
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


#
# registration
#
def register_user(request):
    # look at the request object and see if it has a method POST
    if request.method == 'POST':
        # that will crate form object
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            # save new user
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    # this happend for the 1st time user visits the page
    args = {}
    args.update(csrf(request))

    # give a blank form
    args['form'] = MyRegistrationForm()

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')
