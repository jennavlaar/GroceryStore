from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import *


class RegisterUser(UserCreationForm):
    email = forms.CharField(max_length=120)
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    address = forms.CharField(max_length=120)
    
    class Meta:
        model = RegisteredUser
        fields = ("first_name", "last_name", "address", "email", "username")
    
    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

    
    #dcfgvhbjk@321314