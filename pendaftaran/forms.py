from django import forms
from .models import pendaftaran

from pendaftaran.models import pendaftaran

class formdaftar(forms.ModelForm):
    class Meta:
        model = pendaftaran
        fields = '__all__'


        widgets = {
            'Nama': forms.TextInput({'class':'form-control'}), 
            'Npm':  forms.TextInput({'class':'form-control'}), 
            'Prodi': forms.TextInput({'class':'form-control'}), 
            'Tanggal_lahir': forms.TextInput({'class':'form-control'}), 
            'Alamat': forms.TextInput({'class':'form-control'}), 
            'Kode_pos': forms.TextInput({'class':'form-control'}), 
        }
