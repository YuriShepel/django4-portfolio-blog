from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.short, name='short'),
    path('number', views.short_link, name='short_link')
]