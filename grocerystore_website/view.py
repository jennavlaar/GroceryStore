from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    print(request.user)
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def login(request):
    return render(request, 'login.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')

class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({}, request))