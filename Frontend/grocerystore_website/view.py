from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))