from django.db import models

# Create your models here.
class myvoucher(models.Model):
    kode_voucher = models.CharField(max_length=20)
    kota = models.CharField(max_length=20)
    diskon = models.CharField(max_length=6)
    nama_merch = models.CharField(max_length=30)
    nama_menu = models.CharField(max_length=20)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    alamat = models.CharField(max_length=50)
    info = models.CharField(max_length=256)
    gambar = models.BinaryField(blank=True)

    def __str__(self):
        return self.nama_merch