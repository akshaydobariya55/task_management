from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import SignUpForm , loginform , Add_Project_Form , Add_Task_Form
from django.views.generic.base import RedirectView
from django.contrib import messages
from django.contrib.auth import authenticate , login 
from .models import User , Project , Task ,Comment
from django.views import View

# Create your views here.



def register(request):
    messages = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages = "Register successfully!"
            return redirect('/login/')
        else:
            messages = "Form is not valid"
    else:
        form = SignUpForm()
    return render(request ,'app/registration.html',{'form':form})

def user_login(request):
        if request.method == 'POST':
            form = loginform(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None and user.is_developer:
                    login(request,user)
                    messages.success(request,'Login successfully!')
                    return HttpResponseRedirect('/developer_home/')
                elif user is not None and user.is_manager:
                    login(request,user)
                    messages.success(request,'Login successfully!')
                    return HttpResponseRedirect('/manager_home/')
                else:
                    login(request,user)
                    messages.success(request,'Login successfully!')
                    return HttpResponseRedirect('/admin_home/')
        else:
            form=loginform()
        return render(request , 'app/login.html',{'form':form})


def developer_home(request):
    comment =Comment.objects.all()
    return render(request,'app/developer_home.html',{'comment':comment})

def manager_home(request):
    if request.user.is_authenticated:
        name = request.user
        tasks = Task.objects.filter(list_of_team_member=name)
        return render(request,'app/manager_home.html',{'tasks':tasks})
    else:
        return HttpResponseRedirect('/login/')

def admin_home(request):
    projects = Project.objects.all()
    return render(request,'app/admin_home.html',{'projects':projects})


def add_project(request):
    if request.method == "POST":
        form = Add_Project_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_home/')
    else:
        form = Add_Project_Form()
        form.fields['list_of_team_member'].queryset =User.objects.filter(is_manager=True)
    return render(request,'app/add_project.html',{'form':form})

def add_task(request):
    if request.method == "POST":
        form = Add_Task_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/manager_home/')
    else:
        form = Add_Task_Form()
        form.fields['select_developer'].queryset =User.objects.filter(is_developer=True)
    return render(request,'app/add_task.html',{'form':form})


class projectdeleteview(RedirectView):
    url ='/admin_home/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Project.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
    
class taskdeleteview(RedirectView):
    url ='/manager_home/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Task.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
    
def projectupdateview(request , id):
        if request.method == 'POST':
            pi = Project.objects.get(pk=id)
            form = Add_Project_Form(request.POST,instance=pi)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/admin_home/')
        else:
            pi = Project.objects.get(pk=id)
            form = Add_Project_Form(instance=pi)
        return render(request,'app/update_project.html',{'form':form})

def taskupdateview(request , id):
        if request.method == 'POST':
            pi = Task.objects.get(pk=id)
            form = Add_Task_Form(request.POST,instance=pi)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/manager_home/')
        else:
            pi = Task.objects.get(pk=id)
            form = Add_Task_Form(instance=pi)
        return render(request,'app/update_task.html',{'form':form})
   