from django.shortcuts import render
from django.http import HttpResponse
from communityfund.models import Communities

def index(request):
    context_dict = {'boldmessage': "We are powered by Django!"}
    return render(request, 'communityfund/index.html', context_dict)

def about(request):
    return render(request, 'communityfund/about.html', context_dict)

def login(request):
    return render(request, 'communityfund/login.html')
    
def signup(request):
    context_dict = {'communities': Communities.objects.all()}
    return render(request, 'communityfund/signup.html', context_dict)
    
# Create your views here.
