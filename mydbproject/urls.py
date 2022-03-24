"""mydbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp1 import views

app_name = 'myapp1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('res', views.MyResView.as_view(), name="my_MyResView_view"),
    path('morn', views.MyMornView.as_view(), name="my_MyMornView_view"),
    path('Rooms', views.RoomView.as_view(), name="my_RoomView_view"),
    path('createRoom', views.CreateRoomView.as_view(), name="my_CreateRoomView_view"),
    path('RoomsDisplay', views.RoomDisplayView.as_view(), name="my_RoomDisplayView_view"),
]
