from django import forms

from .models import pinjambuku
from pinjambuku.models import pinjambuku

class Yourform(forms.ModelForm):
    class Meta:
        model = pinjambuku
        fields = '__all__'

        widgets = {
            'Nama': forms.TextInput({'class':'form-control'}),
            'Judul_buku': forms.TextInput({'class':'form-control'}),
            'Pengarang': forms.TextInput({'class':'form-control'}),
            'Tanggal_peminjaman': forms.TextInput({'class':'form-control'}),
            'Alamat': forms.TextInput({'class':'form-control'}),
            'Tanggal_pengembalian': forms.TextInput({'class':'form-control'}),
        }
