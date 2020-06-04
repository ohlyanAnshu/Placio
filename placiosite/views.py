from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
def index(request):
    city = City.objects.all()
    university = University.objects.all()
    return render(request, 'placio/index.html',{'city':city,'university':university})

def postYourRequirement(request):
    if request.method == 'POST':
        form = postYourReq(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.add_message(request,messages.SUCCESS, 'Your requirement ahs been submitted succesfully!')
    else:
         form = postYourReq()
    return render(request, 'placio/postyourreq.html',{'form':form})

def franchise_request(request):
    if request.method == 'POST':
        form1 = franchise(request.POST)
        if form1.is_valid():
            post = form1.save(commit=False)
            post.save()
            messages.add_message(request,messages.SUCCESS, "Your request has been submitted")
    else:
        form1 = franchise()
        return render(request, 'placio/franchise.html',{'form1':form1})


def whyus(request):
    return render(request, 'placio/whyus.html')

def payrent(request):
    if request.method == 'POST':
        form2 = payrentform(request.POST)
        if form2.is_valid():
            post = form2.save(commit=False)
            post.save()
            messages.add_message(request,messages.SUCCESS, "Your rent has been submitted")
    else:
        form2 = payrentform()
        return render(request, 'placio/pay.html',{'form2':form2})

def aboutus(request):
    return render(request, 'placio/aboutus.html')

    