from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from communityfund.models import Communities
from communityfund.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login

def index(request):
    context_dict = {'boldmessage': "We are powered by Django!"}
    return render(request, 'communityfund/index.html', context_dict)

def about(request):
    return render(request, 'communityfund/about.html')

def intro(request):
    return render(request, 'communityfund/intro.html')

def topprojects(request):
    return render(request, 'communityfund/top-projects.html')
    
def projects(request):
    return render(request, 'communityfund/projects.html')
def create(request):
    return render(request, 'communityfund/create.html')
    
def createdetail(request):
    return render(request, 'communityfund/create-details.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Use django's authentication system to verify that the credentials are correct
        user = authenticate(username=username, password=password)
        
        # Check that the user exists
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/communityfund/home')
            else:
                return HttpResponse("Your CommunityFund account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied. Username = " + username + " Password = " + password)
    
    else:
        return render(request, 'communityfund/login.html', {})
    
def signup(request):
    registered = False
    if request.method == 'POST':
        # Grab info from both of the forms on the page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user form data to the DB
            user = user_form.save()
            
            # Hash the user's password
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context_dict = {'communities': Communities.objects.all()}
    return render(request, 'communityfund/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def home(request):
    if request.user.is_authenticated():
        return render(request, 'communityfund/homeL.html')
    else:
        # Temporary work around until we add in user-restricted pages in the next phase
        return render(request, 'communityfund/homeNL.html')

def createproject(request):
    if request.user.is_authenticated():
        return render(request, 'communityfund/create.html')
    else:
        return HttpResponse("Restricted Page. Please login to access.")
        
def intro(request):
    if request.user.is_authenticated():
        return render(request, 'communityfund/indexL.html')
    else:
        return render(request, 'communityfund/indexNL.html')
        
# Create your views here.
