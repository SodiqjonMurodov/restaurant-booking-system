from django.urls import path
from .views import MenuListApiView

urlpatterns = [
    path('menu', MenuListApiView.as_view(), name='menu'),
]