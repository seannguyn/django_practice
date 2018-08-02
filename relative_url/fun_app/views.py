from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'fun_app/index.html')

def relative(request):
    return render(request,'fun_app/relative.html')

def other(request):
    return render(request,'fun_app/other.html')
