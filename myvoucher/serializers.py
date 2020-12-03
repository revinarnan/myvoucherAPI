from rest_framework import serializers
from .models import myvoucher

class myvoucherSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myvoucher
        fields = (
        'id',
        'kode_voucher',
        'kota',
        'diskon',
        'nama_merch',
        'nama_menu',
        'tgl_mulai',
        'tgl_selesai',
        'alamat',
        'gambar',
        )
