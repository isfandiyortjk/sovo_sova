from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_home, name='menu_home')
]



