from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form(request):
    form_0 = forms.FormName()

    if (request.method == "POST"):
        form_0 = forms.FormName(request.POST)

        if form_0.is_valid():
            print("Name: "+form_0.cleaned_data['name'])
            print("Email: "+form_0.cleaned_data['email'])
            print("Text: "+form_0.cleaned_data['text'])

    return render(request,'basicapp/form.html',{'form':form_0})
