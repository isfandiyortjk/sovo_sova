from django.shortcuts import render
from .models import Menu

def menu_home(request):
    tip = Menu.objects.all()
    return render(request,'menu/menu_home.html',{'tip': tip})

