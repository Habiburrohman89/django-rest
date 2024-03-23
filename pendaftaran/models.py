from django.db import models

class pendaftaran(models.Model):
    Nama = models.CharField(max_length=30)
    NPM = models.CharField(max_length=20)
    Prodi = models.CharField(max_length=30)
    Tanggal_lahir = models.DateField()
    Alamat = models.TextField()
    Kode_pos = models.CharField(max_length=5)

    def __str__(self):
        return "{}. {}".format(self.id,self.Nama)
