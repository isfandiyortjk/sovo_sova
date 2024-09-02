from django.urls import path
from .views import IndexView, newsletter_signup,katalog
from . import views

app_name = 'mydjango'
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path('katalog/', katalog, name='katalog'),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
    path('catalog/', views.catalog, name='catalog'),
]