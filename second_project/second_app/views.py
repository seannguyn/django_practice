from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from second_app.models import User

def index(request):
    # return HttpResponse('<em>My Second App</em>')
    return render(request,'second_app/help.html')

def user_data(request):

    user_info = User.objects.all()

    return render(request,'second_app/user_data.html',{'user_info':user_info})
