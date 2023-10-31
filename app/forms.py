from django import forms
from django.contrib.auth.models import User
from .models import User , Project , Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext , gettext_lazy as _
import datetime


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(label='Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email =forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','is_developer','is_manager','is_admin']
        labels = {'email':'Email'}
        widget ={'username':forms.TextInput(attrs={'class':'form-control'})}

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))



class Add_Project_Form(forms.ModelForm):
    start_date = forms.DateField(input_formats=['%d/%m/%Y'], initial=datetime.date.today())
    end_date = forms.DateField(input_formats=['%d/%m/%Y'], initial=datetime.date.today())
    class Meta:
        model = Project
        fields =['name','description','start_date','end_date','list_of_team_member']

class Add_Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title','description','priority','status']