from django.shortcuts import render
from .forms import formdaftar
from.models import pendaftaran

def buku(request):
    return render(request,'buku.html')

def form(request):
    if request.POST:
        form = formdaftar(request.POST)
        if form.is_valid():
            form.save()
            form = formdaftar()
            pesan = 'Data berhasil di simpan'

            kontext = {
                'from': form,
                'pesan': pesan,
            }
            return render(request,'daftarmhs.html',kontext)
    else:
        form = formdaftar()
        kontext = {
            'from' : form,
    }
    return render(request,'daftarmhs.html',kontext)
def model(request):
    daftar = pendaftaran.objects.all()
    context = {
        'daftar': daftar,
    }
    return render(request,'buku.html',context)


