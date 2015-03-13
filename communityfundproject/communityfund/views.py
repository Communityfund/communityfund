from django.shortcuts import render
from django.http import HttpResponse
from communityfund.models import Communities
from communityfund.forms import UserForm, UserProfileForm

def index(request):
    context_dict = {'boldmessage': "We are powered by Django!"}
    return render(request, 'communityfund/index.html', context_dict)

def about(request):
    return render(request, 'communityfund/about.html')

def intro(request):
    return render(reques, 'communityfund/intro.html')

def topprojects(request):
    return render(request, 'communityfund/top-projects.html')
    
def projects(request):
    return render(request, 'communityfund/projects.html')
def create(request):
    return render(request, 'communityfund/create.html')
    
def createdetail(request):
    return render(request, 'communityfund/create-details.html')

def login(request):
    return render(request, 'communityfund/login.html')
    
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
    
# Create your views here.
