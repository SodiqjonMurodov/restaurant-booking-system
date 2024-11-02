from django.urls import path
from .views import CooksHomeListApiView, GalleryHomeListApiView, TestimonialsHomeListApiView, \
    ServicesHomeListApiView, PostsListApiView, PostDetailApiView, GalleryListApiView, CompanyListApiView, \
    DownloadImages, MenuListApiView

urlpatterns = [
    path('home/cooks', CooksHomeListApiView.as_view(), name='home-cooks'),
    path('home/gallery', GalleryHomeListApiView.as_view(), name='home-gallery'),
    path('home/testimonials', TestimonialsHomeListApiView.as_view(), name='home-gallery'),
    path('home/services', ServicesHomeListApiView.as_view(), name='home-gallery'),
    path('posts', PostsListApiView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailApiView.as_view(), name='post'),
    path('gallery', GalleryListApiView.as_view(), name='gallery'),
    path('contacts', CompanyListApiView.as_view(), name='contacts'),
    path('get-image/<int:pk>', DownloadImages.as_view(), name='get-image'),
    path('menu', MenuListApiView.as_view(), name='menu'),

]


