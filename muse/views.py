from rest_framework import generics
from .models import Gallery, Image
from .serializers import GallerySerializer, ImageSerializer

# Create your views here.


class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
