from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from first_app.models import Topic, WebPage, AccessRecors

def index(request):
    mydict = {'key1':'coming from views.py'}
    return render(request,'first_app/index.html',context=mydict)
    # return HttpResponse("hello world")

def static_testing(request):
    return render(request,'first_app/static_testing.html')

def mtv(request):

    access = AccessRecors.objects.order_by('date')
    my_dict = {'accessRecords':access}

    return render(request,'first_app/index0.html',context=my_dict)
