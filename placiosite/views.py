from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
def index(request):
    city = City.objects.all()
    return render(request, 'placio/index.html',{'city':city})

def postYourRequirement(request):
    if request.method == 'POST':
        form = postYourReq(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your requirement ahs been submitted succesfully")
    else:
         form = postYourReq()
    return render(request, 'placio/postyourreq.html',{'form':form})


    