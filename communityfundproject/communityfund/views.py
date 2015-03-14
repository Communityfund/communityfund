from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from communityfund.models import Communities, Interests, UserProfile, CommunityProject
from django.contrib.auth.models import User
from communityfund.forms import UserForm, UserProfileForm, ProjectForm
from django.contrib.auth import authenticate, login, logout

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
    # Load either the logged in or out version of the page
    if request.user.is_authenticated():
        community = UserProfile.objects.all().filter(user=request.user)[0].community
        context_dict = {'projects': CommunityProject.objects.all().filter(community=community)}
        return render(request, 'communityfund/homeL.html', context_dict)
    else:
        # Temporary work around until we add in user-restricted pages in the next phase
        return render(request, 'communityfund/homeNL.html')

def createproject(request):
    # Load either the logged in or out version of the page
    if request.user.is_authenticated():
        context_dict = {'interests': Interests.objects.all()}
        return render(request, 'communityfund/create.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")
        
def intro(request):
    # Load either the logged in or out version of the page
    if request.user.is_authenticated():
        return render(request, 'communityfund/introL.html')
    else:
        return render(request, 'communityfund/introNL.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/communityfund/')

def createdetails(request):
    if request.user.is_authenticated():
        success = False
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST)
            success = project_form.is_valid()
            if project_form.is_valid():
                project = project_form.save(commit=False)
                project.backers = 0
                project.amountFunded = 0
                project.initiator = request.user
                project.community = UserProfile.objects.all().filter(user=request.user)[0].community
                project.save()
                success = True
            else:
                project_form.errors
        else:
            project_form = ProjectForm()
            
        context_dict = {'interests': Interests.objects.all()}
        context_dict['project_form'] = project_form
        context_dict['success'] = success
        return render(request, 'communityfund/create-details.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")
# Create your views here.
