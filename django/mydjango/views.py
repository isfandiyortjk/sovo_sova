from django.http import HttpResponse

from django.views.generic import TemplateView

from django.views.generic import ListView

from .models import Posting
from django.shortcuts import render ,redirect

from .models import Subscriber
from .models import Product

import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    extra_context = {"title": "Base"}
    template_name = "mydjango/index.html"
    


def katalog(request):
    # Логика вашего представления для отображения каталога
    return render(request, 'mydjango/katalog.html')



def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber = Subscriber.objects.create(email=email)
            subscriber.save()
            # Здесь вы можете добавить логику отправки email-сообщения
            return redirect('home')
        except:
            # Обработка ошибок, например, если email уже существует
            pass
    return render(request, 'mydjango/index.html')

def catalog(request):
    products = Product.objects.all()
    return render(request, 'include/catalog.html', {'products': products})