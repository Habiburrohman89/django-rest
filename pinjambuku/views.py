from django.shortcuts import render
from .forms import Yourform
from .models import pinjambuku

def my_view(request):
    if request.POST:
        form = Yourform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Yourform()
        context = {
            'form' : form,
    }
    return render(request,'pinjam.html',context)

def pinjam(request):
    model = pinjambuku.objects.all()
    context ={
        'buku' : model,
    }
    return render(request,'daftarpeminjam.html',context)