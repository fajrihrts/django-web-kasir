from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    jumlah = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.nama