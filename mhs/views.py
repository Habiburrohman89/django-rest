from django.shortcuts import render

def mhs(request):
    return render(request,'index.html')

def nav(request):
    return render(request,'navbar.html')