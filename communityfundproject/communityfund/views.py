from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "We are powered by Django!"}
    return render(request, 'communityfund/index.html', context_dict)

def about(request):
    return HttpResponse("This is the about page for CommunityFund")

def login(request):
    return render(request, 'communityfund/login.html')
    
# Create your views here.
