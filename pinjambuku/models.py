from django.db import models

class pinjambuku(models.Model):
    Nama = models.CharField(max_length=30)
    Judul_buku = models.CharField(max_length=30)
    Pengarang = models.CharField(max_length=30)
    Tanggal_peminjaman = models.DateField()
    Alamat = models.TextField()
    Tanggal_pengembalian = models.DateField()

    def __str__(self):
        return "{}. {}".format(self.id,self.Nama)
