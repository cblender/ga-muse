from rest_framework import serializers
from .models import Gallery, Image


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name="image_detail")

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'images')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    gallery_id = serializers.PrimaryKeyRelatedField(
        queryset=Gallery.objects.all())

    class Meta:
        model = Image
        fields = ('id', 'name', 'img_url', 'gallery_id')
