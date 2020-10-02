from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.GalleryList.as_view(), name='gallery_list'),
    path('gallery/<int:pk>', views.GalleryDetail.as_view(), name='gallery_detail'),
    path('image/', views.ImageList.as_view(), name='image_list'),
    path('image/<int:pk>', views.ImageDetail.as_view(), name='image_detail'),

]
