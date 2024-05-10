from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('lol/', views.lol, name='lol'),
    path('about_the_site/', views.about_the_site, name='about_the_site'),
    
]