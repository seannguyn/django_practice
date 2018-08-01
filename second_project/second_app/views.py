from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from second_app.models import User
from . import forms


def index(request):
    # return HttpResponse('<em>My Second App</em>')
    return render(request,'second_app/help.html')

def user_data(request):

    user_info = User.objects.all()

    return render(request,'second_app/user_data.html',{'user_info':user_info})

def signup(request):
    form_0 = forms.FormName()

    if (request.method=="POST"):
        form_0 = forms.FormName(request.POST)

        if (form_0.is_valid()):
            t = User.objects.get_or_create(name=form_0.cleaned_data['form_name'],
                                            email=form_0.cleaned_data['form_email'],
                                            password=form_0.cleaned_data['form_password'])[0]
            t.save()
            return render(request,'second_app/help.html')

    return render(request,'second_app/signup.html',{'form':form_0})

def signup_(request):
    form_0 = forms.UserForm()

    if (request.method=="POST"):
        form_0 = forms.UserForm(request.POST)

        if (form_0.is_valid()):
            form_0.save(commit=True)
            return index(request)

    return render(request,'second_app/signup.html',{'form':form_0})
