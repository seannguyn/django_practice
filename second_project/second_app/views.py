from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<em>My Second App</em>')
    return render(request,'second_app/help.html')
