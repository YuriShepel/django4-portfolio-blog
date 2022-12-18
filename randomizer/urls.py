from django.urls import path
from . import views

app_name = 'randomizer'

urlpatterns = [
    path('', views.generate_number, name='number_generator'),
    path('number', views.random_number, name='number')
]