from django.shortcuts import render
from rest_framework import viewsets

from .serializers import myvoucherSerializers
from .models import myvoucher

# Create your views here.
class myvoucherViewSet(viewsets.ModelViewSet):
    queryset = myvoucher.objects.all().order_by('id')
    serializer_class = myvoucherSerializers
    
#def image(request):
#    image_file = request.FILES['image_file'].file.read()
#    myvoucher.objects.create(gambar=image_file)
