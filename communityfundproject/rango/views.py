from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "Django!"}
    return render(request, 'rango/about.html', context_dict)

# Create your views here.
