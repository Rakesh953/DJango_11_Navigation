from django.shortcuts import render

# Create your views here.

def navigate(request):
    return render(request,'navigate1.html')

def navigate2(request):
    return render(request,'navigate2.html')
