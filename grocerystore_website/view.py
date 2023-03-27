from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .gs.models import *
from .gs.forms import RegisterUser
from django.contrib import messages
from django.shortcuts import  render, redirect

def home(request):
    print(request.user)
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def login(request, user):
    if request.method == 'GET':
        context = ''
        return render(request, 'login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'context': context})
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'login.html')
        
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #name = form.cleaned_data['name']
            #address = form.cleaned_data['address']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})



def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))