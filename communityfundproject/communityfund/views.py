from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from communityfund.models import Communities, Interests, UserProfile, CommunityProject, Payment, Comment, ProjectComment, UserInterest
from django.contrib.auth.models import User
from communityfund.forms import UserForm, UserProfileForm, ProjectForm, PaymentForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.db.models import Sum

def index(request):
    context_dict = {'boldmessage': "We are powered by Django!"}
    return render(request, 'communityfund/index.html', context_dict)

def about(request):
    return render(request, 'communityfund/about.html')

def topprojects(request):
    return render(request, 'communityfund/top-projects.html')
    
def editprofile(request):
    return render(request, 'communityfund/editprofile.html')

def find(request):
    return render(request, 'communityfund/find.html')

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
            return HttpResponse("Invalid login details supplied.")
    
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
        # If the user is logged in, load all of the projects the user as donated to,
        # all of their projects, and all other projects.
        
        # Get the user's contributed to projects
        p = Payment.objects.all().filter(backer=request.user).values('project').distinct()
        contributed = CommunityProject.objects.all().filter(pk__in=p)
        # Get the user's own projects
        ownprojects = CommunityProject.objects.all().filter(initiator=request.user)
        
        # Get all the other projects
        community = UserProfile.objects.all().filter(user=request.user)[0].community
        allprojects = CommunityProject.objects.all().filter(community=community)
        
        context_dict = {'allprojects': CommunityProject.objects.all().filter(community=community)}
        context_dict['contributed'] = contributed
        context_dict['ownprojects'] = ownprojects
        
    else:
        # If the user is not logged in, just load all of the projects in the database
        context_dict = {'allprojects': CommunityProject.objects.all()}

    return render(request, 'communityfund/home.html', context_dict)

def createproject(request):
    # Only allow logged in users to create a project
    if request.user.is_authenticated():
        success = False
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST)
            if project_form.is_valid():
                project = project_form.save(commit=False)
                project.backers = 0
                project.amountFunded = 0
                project.initiator = request.user
                project.community = UserProfile.objects.all().filter(user=request.user)[0].community
                project.dateCreated = datetime.now()
                
                if 'picture' in request.FILES:
                    project.picture = request.FILES['picture']
                    
                project.save()
                success = True
            else:
                project_form.errors
        else:
            project_form = ProjectForm()
        
        # 'GET' was received, so load the page
        context_dict = {'interests': Interests.objects.all()}
        context_dict['project_form'] = project_form
        context_dict['success'] = success
        return render(request, 'communityfund/createproject.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")

def intro(request):
    # Load either the logged in or out version of the page
    if request.user.is_authenticated():
        return render(request, 'communityfund/introL.html')
    else:
        return render(request, 'communityfund/introNL.html')

# Log out the user
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/communityfund/')

def createdetails(request):
    # Only allow logged in users to create a project.
    if request.user.is_authenticated():
        success = False
        
        # If a 'POST' was received, submit the form info to the database
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST)
            if project_form.is_valid():
                project = project_form.save(commit=False)
                project.backers = 0
                project.amountFunded = 0
                project.initiator = request.user
                project.community = UserProfile.objects.all().filter(user=request.user)[0].community
                
                if 'picture' in request.FILES:
                    project.picture = request.FILES['picture']
                    
                project.save()
                success = True
            else:
                project_form.errors
        else:
            project_form = ProjectForm()
        
        # 'GET' was received, so load the page
        context_dict = {'interests': Interests.objects.all()}
        context_dict['project_form'] = project_form
        context_dict['success'] = success
        return render(request, 'communityfund/create-details.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")

def profile(request, profile_name):
    context_dict = {}
    
    try:
        user_info = User.objects.all().filter(username=profile_name)
        user_profile = UserProfile.objects.all().filter(user=user_info)
        user_projects = CommunityProject.objects.all().filter(initiator=user_info)
        backed_projects = Payment.objects.all().filter(backer=user_info).values('project')
        interests = UserInterest.objects.all().filter(user=user_info)
        
        context_dict['user_info'] = user_info
        context_dict['user_profile'] = user_profile
        context_dict['user_projects'] = user_projects
        context_dict['backed_projects'] = backed_projects
        context_dict['interests'] = interests
        
    except (User.DoesNotExist, UserProfile.DoesNotExist) as e:
        pass
    return render(request, 'communityfund/profile.html', context_dict)

def projects(request, project_name):
    context_dict = {}
    
    try:
        p = CommunityProject.objects.all().filter(slug=project_name)
        if p:
            p = p[0]
        u = p.initiator
        profile = UserProfile.objects.all().filter(user=u)
        if profile:
            profile = profile[0]
        
        context_dict['project'] = p
        context_dict['profile'] = profile
    except CommunityProject.DoesNotExist:
        pass
    return render(request, 'communityfund/project.html', context_dict)

def payment(request, project_name):
    if request.user.is_authenticated():
        context_dict = {}
        success = False
        if request.method == 'POST':
            payment_form = PaymentForm(data=request.POST)
            if payment_form.is_valid():
                project = CommunityProject.objects.get(slug=project_name)
                profile = UserProfile.objects.get(user=request.user)
                # Insert the payment info
                payment = payment_form.save(commit=False)
                payment.backer = request.user
                payment.project = project
                payment.timestamp = datetime.now()
            
                # Update the project info
                CommunityProject.objects.all().filter(slug=project_name).update(amountFunded=project.amountFunded + payment.amount,
                                                                                backers=project.backers+1)
            
                # Update the user's info (and the project initiator's if the project is fully funded)
                UserProfile.objects.all().filter(user=request.user).update(reputation=profile.reputation+1,
                                                                           projectsFunded=profile.projectsFunded+1)
                if (project.amountFunded < project.goal):
                    project_initiator = UserProfile.objects.all().filter(user=project.initiator)[0]
                    UserProfile.objects.all().filter(user=project.initiator).update(reputation=project_initiator.reputation+10)
            
                payment.save()
                success = True
            else:
                payment_form.errors
        else:
            payment_form = PaymentForm()
        context_dict['payment_form'] = payment_form
        context_dict['success'] = success
        context_dict['project_name'] = project_name
        return render(request, 'communityfund/payment.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")

def settings(request):
    if request.user.is_authenticated():
        context_dict = {}
        projects_started = CommunityProject.objects.all().filter(initiator=request.user).count()
        projects_funded = Payment.objects.all().filter(backer=request.user).distinct().count()
        money_raised = Payment.objects.all().filter(backer=request.user).aggregate(Sum('amount'))
        
        context_dict['projects_started'] = projects_started
        context_dict['projects_funded'] = projects_funded
        context_dict['money_raised'] = money_raised
        return render(request, 'communityfund/settings.html', context_dict)
    else:
        return HttpResponse("Restricted Page. Please login to access.")
# Create your views here.
